#!/usr/bin/env python3
"""In-memory DuckDB runner for the SQL interview practice suite.

Usage (from this folder):
    python3 run.py 24                 check your answer in problems/24_*.sql
    python3 run.py 24 --show          print the problem prompt
    python3 run.py 24 --solution      run and print the reference solution
    python3 run.py --all              progress board for every problem
    python3 run.py --solutions        verify every reference solution (suite self-check)
    python3 run.py --schema hr        show tables and sample rows for a dataset
    python3 run.py --scratch 24 "SELECT * FROM logins LIMIT 5"
    python3 run.py --random hard      pick an unsolved problem
"""
import argparse
import datetime as dt
import decimal
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent

try:
    import duckdb
except ImportError:
    raise SystemExit("duckdb is not installed in this Python. Use the repo virtual environment:\n"
                     "    source ../../.venv/bin/activate     (from data_engineering/sql_practice)\n"
                     "or run through it directly: make app / make all / make test.\n"
                     "First time? `make setup` creates the venv and installs requirements.txt.")

from catalog import PROBLEMS, TOPICS, by_id  # noqa: E402

DATASETS_DIR = HERE / "datasets"
PROBLEMS_DIR = HERE / "problems"
SOLUTIONS_DIR = HERE / "solutions"
EXPECTED_DIR = HERE / "expected"
ANSWER_MARKER = "-- YOUR SQL BELOW"
FLOAT_PLACES = 2


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def connect(problem):
    con = duckdb.connect(":memory:")
    for name in problem.datasets:
        con.execute((DATASETS_DIR / f"{name}.sql").read_text())
    return con


def strip_comments(sql):
    sql = re.sub(r"/\*.*?\*/", "", sql, flags=re.S)
    return "\n".join(line.split("--", 1)[0] for line in sql.splitlines()).strip()


def read_attempt(problem):
    text = (PROBLEMS_DIR / problem.filename).read_text()
    if ANSWER_MARKER in text:
        text = text.split(ANSWER_MARKER, 1)[1]
    return text if strip_comments(text) else None


def read_solution(problem):
    return (SOLUTIONS_DIR / problem.filename).read_text()


def read_expected(problem):
    path = EXPECTED_DIR / f"{problem.key}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())


def run_query(con, sql):
    con.execute(sql)
    columns = [d[0] for d in con.description] if con.description else []
    return columns, con.fetchall()


# ---------------------------------------------------------------------------
# Normalization and comparison
# ---------------------------------------------------------------------------

def normalize(value):
    if value is None or isinstance(value, (bool, str)):
        return value
    if isinstance(value, (int, float, decimal.Decimal)):
        return round(float(value), FLOAT_PLACES) + 0.0
    if isinstance(value, dt.datetime):
        return value.isoformat(sep=" ")
    if isinstance(value, (dt.date, dt.time)):
        return value.isoformat()
    if isinstance(value, dt.timedelta):
        return str(value)
    if isinstance(value, (list, tuple)):
        return tuple(normalize(v) for v in value)
    if isinstance(value, dict):
        return tuple(sorted((k, normalize(v)) for k, v in value.items()))
    return str(value)


def normalize_rows(rows):
    return [tuple(normalize(v) for v in row) for row in rows]


def to_json_value(value):
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    value = normalize(value)
    return list(value) if isinstance(value, tuple) else value


def diff(problem, rows):
    """Compare actual rows against expected/NN.json.

    Returns a dict with ok, reason (None, "missing_expected", "columns", "order", or "rows"),
    expected_columns, expected_count, got_count, missing, and extra.
    """
    expected = read_expected(problem)
    result = {"ok": False, "reason": None, "expected_columns": [], "expected_count": 0,
              "got_count": len(rows), "missing": [], "extra": []}
    if expected is None:
        result["reason"] = "missing_expected"
        return result
    want = normalize_rows(expected["rows"])
    got = normalize_rows(rows)
    result["expected_columns"] = expected["columns"]
    result["expected_count"] = len(want)

    if got and want and len(got[0]) != len(want[0]):
        result["reason"] = "columns"
        return result

    if problem.ordered:
        if got == want:
            result["ok"] = True
            return result
        if Counter(got) == Counter(want):
            result["reason"] = "order"
            return result
    elif Counter(got) == Counter(want):
        result["ok"] = True
        return result

    result["reason"] = "rows"
    result["missing"] = list((Counter(want) - Counter(got)).elements())
    result["extra"] = list((Counter(got) - Counter(want)).elements())
    return result


def compare(problem, rows):
    """Return (ok, message) comparing actual rows against expected/NN.json."""
    d = diff(problem, rows)
    if d["ok"]:
        return True, "PASS"
    if d["reason"] == "missing_expected":
        return False, f"No expected/{problem.key}.json yet. Run --freeze {problem.id} after checking the solution."
    if d["reason"] == "columns":
        return False, (f"Column count mismatch: expected {len(d['expected_columns'])} columns "
                       f"({', '.join(d['expected_columns'])}), got {len(rows[0])}.")
    if d["reason"] == "order":
        return False, "Right rows, wrong order. This problem requires a specific ORDER BY."

    lines = [f"Expected {d['expected_count']} rows, got {d['got_count']}."]
    if d["missing"]:
        lines.append("Missing rows (expected but not returned):")
        lines += [f"  - {r}" for r in d["missing"]]
    if d["extra"]:
        lines.append("Extra rows (returned but not expected):")
        lines += [f"  + {r}" for r in d["extra"]]
    if problem.ordered and not d["missing"] and not d["extra"]:
        lines.append("Row order differs from the expected order.")
    return False, "\n".join(lines)


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def format_table(columns, rows, limit=40):
    shown = [[("NULL" if v is None else str(v)) for v in row] for row in rows[:limit]]
    widths = [len(c) for c in columns]
    for row in shown:
        widths = [max(w, len(v)) for w, v in zip(widths, row)]
    sep = "+".join("-" * (w + 2) for w in widths)
    out = [" | ".join(c.ljust(w) for c, w in zip(columns, widths)), sep]
    out += [" | ".join(v.ljust(w) for v, w in zip(row, widths)) for row in shown]
    if len(rows) > limit:
        out.append(f"... {len(rows) - limit} more rows")
    out.append(f"({len(rows)} rows)")
    return "\n".join(out)


def header(problem):
    return f"[{problem.key}] {problem.title}  ({problem.difficulty}, {problem.topic})"


def evaluate(problem, sql):
    """Return (status, detail, columns, rows). Status is PASS, FAIL, ERROR, or TODO."""
    if sql is None:
        return "TODO", "No SQL written yet.", [], []
    con = connect(problem)
    try:
        columns, rows = run_query(con, sql)
    except duckdb.Error as exc:
        return "ERROR", f"{type(exc).__name__}: {exc}", [], []
    ok, message = compare(problem, rows)
    return ("PASS" if ok else "FAIL"), message, columns, rows


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_check(problem, use_solution=False):
    sql = read_solution(problem) if use_solution else read_attempt(problem)
    print(header(problem))
    print(f"File: {(SOLUTIONS_DIR if use_solution else PROBLEMS_DIR).name}/{problem.filename}\n")
    status, detail, columns, rows = evaluate(problem, sql)
    if status == "TODO":
        print(f"TODO: write your query below '{ANSWER_MARKER}' in problems/{problem.filename}")
        return 1
    if columns:
        print(format_table(columns, rows))
        print()
    print(status if status == "PASS" else f"{status}\n{detail}")
    if status == "PASS" and not use_solution:
        print(f"\nCompare with solutions/{problem.filename} for the approach and the trap it avoids.")
    return 0 if status == "PASS" else 1


def cmd_show(problem):
    text = (PROBLEMS_DIR / problem.filename).read_text()
    print(text.split(ANSWER_MARKER, 1)[0].rstrip())
    return 0


def cmd_all(use_solutions=False):
    totals = Counter()
    for topic in TOPICS:
        print(f"\n{topic}")
        for p in (p for p in PROBLEMS if p.topic == topic):
            sql = read_solution(p) if use_solutions else read_attempt(p)
            status, detail, _, _ = evaluate(p, sql)
            totals[status] += 1
            print(f"  {status:<5} {p.key} {p.title} ({p.difficulty})")
            if use_solutions and status != "PASS":
                print("        " + detail.replace("\n", "\n        "))
    print("\n" + "  ".join(f"{k}: {v}" for k, v in sorted(totals.items())) + f"  (of {len(PROBLEMS)})")
    return 0 if totals["PASS"] == len(PROBLEMS) else 1


def cmd_schema(name):
    path = DATASETS_DIR / f"{name}.sql"
    if not path.exists():
        names = ", ".join(sorted(p.stem for p in DATASETS_DIR.glob("*.sql")))
        raise SystemExit(f"Unknown dataset {name!r}. Available: {names}")
    con = duckdb.connect(":memory:")
    con.execute(path.read_text())
    for (table,) in con.execute("SELECT table_name FROM information_schema.tables ORDER BY table_name").fetchall():
        cols = con.execute(
            "SELECT column_name, data_type FROM information_schema.columns "
            "WHERE table_name = ? ORDER BY ordinal_position", [table]).fetchall()
        count = con.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
        print(f"\n== {table} ({count} rows): " + ", ".join(f"{c} {t}" for c, t in cols))
        columns, rows = run_query(con, f'SELECT * FROM "{table}" LIMIT 8')
        print(format_table(columns, rows, limit=8))
    return 0


def cmd_scratch(problem, sql):
    con = connect(problem)
    try:
        columns, rows = run_query(con, sql)
    except duckdb.Error as exc:
        print(f"{type(exc).__name__}: {exc}")
        return 1
    print(format_table(columns, rows, limit=200))
    return 0


def cmd_random(level):
    pool = [p for p in PROBLEMS if level in ("any", p.difficulty)]
    unsolved = [p for p in pool if evaluate(p, read_attempt(p))[0] != "PASS"]
    if not unsolved:
        print("Everything in that pool passes. Reset a file or pick another level.")
        return 0
    p = random.choice(unsolved)
    print(f"Your problem: problems/{p.filename}  ({'25' if p.difficulty == 'hard' else '15'} minute timer)\n")
    return cmd_show(p)


def cmd_freeze(problems):
    """Write expected/NN.json from the reference solution. Maintainer use only."""
    EXPECTED_DIR.mkdir(exist_ok=True)
    for p in problems:
        con = connect(p)
        columns, rows = run_query(con, read_solution(p))
        body = ",\n  ".join(json.dumps([to_json_value(v) for v in row]) for row in rows)
        text = f'{{\n "columns": {json.dumps(columns)},\n "rows": [\n  {body}\n ]\n}}\n'
        (EXPECTED_DIR / f"{p.key}.json").write_text(text)
        print(f"froze {p.key}: {len(rows)} rows")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("problem", nargs="?", help="problem number, e.g. 24")
    parser.add_argument("--show", action="store_true", help="print the problem prompt")
    parser.add_argument("--solution", action="store_true", help="run the reference solution for PROBLEM")
    parser.add_argument("--all", action="store_true", help="progress board for your attempts")
    parser.add_argument("--solutions", action="store_true", help="verify every reference solution")
    parser.add_argument("--schema", metavar="DATASET", help="show tables in a dataset")
    parser.add_argument("--scratch", nargs=2, metavar=("PROBLEM", "SQL"), help="run ad-hoc SQL on a problem's data")
    parser.add_argument("--random", nargs="?", const="any", choices=["any", "medium", "hard"],
                        help="pick a random unsolved problem")
    parser.add_argument("--freeze", nargs="+", metavar="PROBLEM", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    if args.all or args.solutions:
        return cmd_all(use_solutions=args.solutions)
    if args.schema:
        return cmd_schema(args.schema)
    if args.scratch:
        return cmd_scratch(by_id(args.scratch[0]), args.scratch[1])
    if args.random:
        return cmd_random(args.random)
    if args.freeze:
        targets = PROBLEMS if args.freeze == ["all"] else [by_id(x) for x in args.freeze]
        return cmd_freeze(targets)
    if args.problem:
        problem = by_id(args.problem)
        if args.show:
            return cmd_show(problem)
        return cmd_check(problem, use_solution=args.solution)
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
