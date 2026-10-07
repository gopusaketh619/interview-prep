#!/usr/bin/env python3
"""Browser UI for the SQL practice suite.

    python3 app.py               serve on http://127.0.0.1:8765 and open a browser tab
    python3 app.py --port 9000   pick another port
    python3 app.py --no-browser  do not open a tab

Answers are saved to problems/NN_slug.sql, the same files the CLI reads, so
`python3 run.py --all` and the web UI always agree. Standard library only (plus duckdb).
"""
import argparse
import datetime as dt
import decimal
import json
import math
import re
import threading
import time
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import run
from run import ANSWER_MARKER, PROBLEMS_DIR, duckdb
from catalog import PROBLEMS, TOPICS

WEB_DIR = run.HERE / "web"
STATIC = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
}
QUERY_TIMEOUT_S = 10
MAX_RESULT_ROWS = 500
SAMPLE_ROWS = 5
_BY_ID = {p.id: p for p in PROBLEMS}


class QueryError(Exception):
    pass


# ---------------------------------------------------------------------------
# Problem files
# ---------------------------------------------------------------------------

def _comment_lines(text):
    return [re.sub(r"^--\s?", "", line) for line in text.splitlines()]


def parse_prompt(problem):
    """Split a problem file header into display fields."""
    header = (PROBLEMS_DIR / problem.filename).read_text().split(ANSWER_MARKER, 1)[0]
    lines = _comment_lines(header.strip())
    rulers = [i for i, line in enumerate(lines) if re.fullmatch(r"=+", line.strip())]
    meta = " ".join(line.strip() for line in lines[rulers[0] + 2:rulers[1]])
    body = lines[rulers[1] + 1:rulers[2]]

    def meta_field(name, nxt):
        m = re.search(rf"{name}:\s*(.*?)\s*(?:{nxt}:|$)", meta)
        return m.group(1) if m else ""

    fields = {"output_columns": "", "row_order": ""}
    description, key, in_tail = [], None, False
    for line in body:
        m = re.match(r"(Output columns|Row order|Check):\s*(.*)", line)
        if m:
            in_tail = True
            key = {"Output columns": "output_columns", "Row order": "row_order"}.get(m.group(1))
            if key:
                fields[key] = m.group(2).strip()
        elif in_tail:
            if key and line.startswith(" ") and line.strip():
                fields[key] += " " + line.strip()
        else:
            description.append(line.rstrip())
    while description and not description[-1].strip():
        description.pop()

    return {
        "inspired_by": meta_field("Inspired by", "Tables"),
        "tables": [t.strip() for t in meta_field("Tables", "Schema").split(",") if t.strip()],
        "description": description,
        **fields,
    }


def read_editor_sql(problem):
    text = (PROBLEMS_DIR / problem.filename).read_text()
    return text.split(ANSWER_MARKER, 1)[1].strip() if ANSWER_MARKER in text else ""


def write_attempt(problem, sql):
    path = PROBLEMS_DIR / problem.filename
    head = path.read_text().split(ANSWER_MARKER, 1)[0] + ANSWER_MARKER + "\n\n"
    sql = sql.strip()
    path.write_text(head + (sql + "\n" if sql else ""))


# ---------------------------------------------------------------------------
# Query execution
# ---------------------------------------------------------------------------

def jsonable(value):
    if value is None or isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, float):
        return value if math.isfinite(value) else str(value)
    if isinstance(value, decimal.Decimal):
        return str(value)
    if isinstance(value, dt.datetime):
        return value.isoformat(sep=" ")
    if isinstance(value, (dt.date, dt.time)):
        return value.isoformat()
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    return str(value)


def execute(problem, sql):
    """Run SQL on a fresh copy of the problem's data. Returns (columns, types, rows, ms)."""
    con = run.connect(problem)
    timer = threading.Timer(QUERY_TIMEOUT_S, con.interrupt)
    timer.start()
    started = time.perf_counter()
    try:
        con.execute(sql)
        desc = con.description or []
        rows = con.fetchall() if desc else []
    except duckdb.Error as exc:
        if not timer.is_alive():
            raise QueryError(f"Query cancelled after {QUERY_TIMEOUT_S}s. Check for a runaway join or recursive CTE.")
        raise QueryError(f"{type(exc).__name__}: {exc}")
    finally:
        timer.cancel()
        con.close()
    ms = round((time.perf_counter() - started) * 1000, 1)
    return [d[0] for d in desc], [str(d[1]) for d in desc], rows, ms


def result_payload(columns, types, rows, ms):
    return {
        "columns": columns,
        "types": types,
        "rows": jsonable(rows[:MAX_RESULT_ROWS]),
        "total": len(rows),
        "truncated": len(rows) > MAX_RESULT_ROWS,
        "ms": ms,
    }


_status_cache = {}


def grade(problem, sql):
    """Return (status, payload). Status is PASS, FAIL, ERROR, or TODO."""
    if not run.strip_comments(sql or ""):
        return "TODO", {"message": "No SQL written yet."}
    try:
        columns, types, rows, ms = execute(problem, sql)
    except QueryError as exc:
        return "ERROR", {"message": str(exc)}
    d = run.diff(problem, rows)
    _, message = run.compare(problem, rows)
    payload = result_payload(columns, types, rows, ms)
    payload.update(message=message, reason=d["reason"], expected_columns=d["expected_columns"],
                   expected_count=d["expected_count"], missing=d["missing"], extra=d["extra"])
    return ("PASS" if d["ok"] else "FAIL"), payload


def cached_status(problem):
    sql = read_editor_sql(problem)
    key = (problem.id, sql)
    if key not in _status_cache:
        _status_cache[key] = grade(problem, sql)[0]
    return _status_cache[key]


def schema(problem):
    con = run.connect(problem)
    try:
        tables = []
        names = con.execute(
            "SELECT table_name FROM information_schema.tables ORDER BY table_name").fetchall()
        for (name,) in names:
            cols = con.execute(
                "SELECT column_name, data_type FROM information_schema.columns "
                "WHERE table_name = ? ORDER BY ordinal_position", [name]).fetchall()
            count = con.execute(f'SELECT COUNT(*) FROM "{name}"').fetchone()[0]
            sample = con.execute(f'SELECT * FROM "{name}" LIMIT {SAMPLE_ROWS}').fetchall()
            tables.append({
                "name": name,
                "count": count,
                "columns": [{"name": c, "type": t} for c, t in cols],
                "sample": jsonable(sample),
            })
        return tables
    finally:
        con.close()


def summary(problem):
    return {"id": problem.id, "key": problem.key, "title": problem.title, "topic": problem.topic,
            "difficulty": problem.difficulty, "ordered": problem.ordered, "filename": problem.filename}


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

ROUTE = re.compile(r"^/api/problems/(\d+)(?:/(run|save|submit|reset|solution))?$")


class Handler(BaseHTTPRequestHandler):
    server_version = "SQLPractice/1.0"

    def log_message(self, fmt, *args):
        pass

    def send_json(self, data, status=HTTPStatus.OK):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(length) or b"{}")

    def problem_or_404(self, pid):
        problem = _BY_ID.get(int(pid))
        if problem is None:
            self.send_json({"error": f"Unknown problem {pid}"}, HTTPStatus.NOT_FOUND)
        return problem

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in STATIC:
            filename, ctype = STATIC[path]
            body = (WEB_DIR / filename).read_bytes()
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        if path == "/api/problems":
            items = [{**summary(p), "status": cached_status(p)} for p in PROBLEMS]
            self.send_json({"problems": items, "topics": TOPICS})
            return
        m = ROUTE.match(path)
        if not m or m.group(2) not in (None, "solution"):
            self.send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
            return
        problem = self.problem_or_404(m.group(1))
        if problem is None:
            return
        if m.group(2) == "solution":
            self.send_json({"sql": run.read_solution(problem)})
            return
        self.send_json({**summary(problem), **parse_prompt(problem), "datasets": list(problem.datasets),
                        "sql": read_editor_sql(problem), "schema": schema(problem),
                        "status": cached_status(problem)})

    def do_POST(self):
        m = ROUTE.match(self.path)
        if not m or m.group(2) in (None, "solution"):
            self.send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
            return
        problem = self.problem_or_404(m.group(1))
        if problem is None:
            return
        action = m.group(2)
        sql = self.read_json().get("sql", "")

        if action == "run":
            if not run.strip_comments(sql):
                self.send_json({"error": "Nothing to run."})
                return
            try:
                self.send_json(result_payload(*execute(problem, sql)))
            except QueryError as exc:
                self.send_json({"error": str(exc)})
        elif action == "save":
            write_attempt(problem, sql)
            self.send_json({"saved": True})
        elif action == "reset":
            write_attempt(problem, "")
            self.send_json({"saved": True, "status": "TODO"})
        elif action == "submit":
            write_attempt(problem, sql)
            status, payload = grade(problem, sql)
            _status_cache[(problem.id, read_editor_sql(problem))] = status
            self.send_json({"status": status, **payload})


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}/"
    print(f"SQL practice UI running at {url}  (Ctrl+C to stop)")
    if not args.no_browser:
        threading.Timer(0.5, webbrowser.open, [url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
