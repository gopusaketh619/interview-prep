# SQL Practice Suite for Data Engineering Interviews

50 medium-to-hard SQL problems that run against an in-memory [DuckDB](https://duckdb.org/) database. You write your query in a problem file, the runner loads fresh data, runs your SQL, and diffs the result against the expected output. Reference solutions explain the approach and the specific trap each dataset is built to catch.

Problems are modeled on LeetCode SQL 50 / Top SQL, DataLemur, StrataScratch, and questions reported from Meta, Amazon, Airbnb, Uber, Stripe, and Netflix data engineering loops. DuckDB's dialect (QUALIFY, `date_trunc`, `FILTER`, `PIVOT`, ASOF joins) is close to Snowflake, BigQuery, and Databricks SQL.

---

## Setup

```bash
cd interview_prep/sql_practice
python3 -m pip install -r requirements.txt   # duckdb + pytest
```

If you cannot install globally, `python3 -m pip install --target .deps duckdb` also works; `run.py` picks up `.deps/` automatically.

---

## Workflow

1. Pick a problem and read the prompt: `python3 run.py 24 --show`
2. Look at the data: `python3 run.py --schema events`
3. Explore while you think: `python3 run.py --scratch 24 "SELECT * FROM logins WHERE user_id = 1"`
4. Write your query below `-- YOUR SQL BELOW` in `problems/24_longest_login_streak.sql`
5. Check it: `python3 run.py 24`
6. After it passes (or after your timer runs out), read `solutions/24_longest_login_streak.sql`

On failure the runner prints your output plus the exact missing and extra rows:

```
FAIL
Expected 5 rows, got 5.
Missing rows (expected but not returned):
  - ('Marketing', None)
Extra rows (returned but not expected):
  + ('Marketing', 95000.0)
```

### All commands

| Command | What it does |
|---|---|
| `python3 run.py 24` | Check your answer |
| `python3 run.py 24 --show` | Print the prompt |
| `python3 run.py 24 --solution` | Run and print the reference solution |
| `python3 run.py --all` | Progress board (PASS / FAIL / ERROR / TODO) by topic |
| `python3 run.py --random hard` | Random unsolved problem with a timer suggestion (`medium`, `hard`, or `any`) |
| `python3 run.py --schema hr` | Tables, column types, and sample rows for a dataset |
| `python3 run.py --scratch 24 "SQL"` | Ad-hoc query against a problem's data |
| `python3 run.py --solutions` | Self-check: every reference solution must pass |
| `pytest` | Same checks via pytest; unattempted problems are skipped |
| `SQL_SOLUTIONS=1 pytest` | Run pytest against the reference solutions |

### Comparison rules

- Numbers are compared rounded to 2 decimals; `150`, `150.0`, and `DECIMAL 150.00` are equal.
- Dates and timestamps are compared as ISO strings, so `DATE` vs `VARCHAR '2025-01-05'` both work.
- Column names are ignored, but the number of columns must match the prompt.
- Row order only matters when the prompt says so (`Row order: ...`).

---

## Problem index

| # | Problem | Topic | Level |
|---|---|---|---|
| 01 | Customers who never ordered | Joins | M |
| 02 | Second-highest salary per department | Joins | M |
| 03 | Products frequently bought together | Joins | H |
| 04 | Customers who bought every Electronics product | Joins (relational division) | H |
| 05 | Friend recommendations by mutual friends | Joins | H |
| 06 | Monthly transactions by country | Aggregation | M |
| 07 | Departments above the company average salary | Aggregation | M |
| 08 | Median salary per department (no MEDIAN) | Aggregation | H |
| 09 | Histogram of posts per user | Aggregation | M |
| 10 | Percentage of immediate first orders | Aggregation | M |
| 11 | Top 3 distinct salaries per department | Ranking | H |
| 12 | Top-selling product per category per month | Ranking | M |
| 13 | Top 2 grossing products per category | Ranking | M |
| 14 | Top-quartile customers by spend | Ranking (NTILE) | M |
| 15 | Employees whose salary rank dropped | Ranking | H |
| 16 | Each user's third transaction | Ranking | M |
| 17 | Running revenue that resets each month | Window aggregates | M |
| 18 | 7-day rolling average with missing days | Window aggregates + date spine | H |
| 19 | Month-over-month revenue growth | LAG | M |
| 20 | Year-over-year spend growth per product | LAG / period join | M |
| 21 | Last person to fit on the bus | Running sum | M |
| 22 | Warmer than the previous calendar day | LAG vs date math | M |
| 23 | Numbers appearing 3+ times consecutively | Gaps and islands | M |
| 24 | Longest login streak per user | Gaps and islands | H |
| 25 | 3+ consecutive high-traffic rows | Gaps and islands | H |
| 26 | Collapse ids into continuous ranges | Gaps and islands | M |
| 27 | Compress daily run states into periods | Gaps and islands | H |
| 28 | Sessionize a clickstream | Sessionization | H |
| 29 | Ordered conversion funnel within 7 days | Funnels | H |
| 30 | Average days from first to second order | Event analytics | M |
| 31 | Fraction of players back the day after first login | Event analytics | M |
| 32 | Peak concurrent sessions (min meeting rooms) | Sweep line | H |
| 33 | Month-over-month retained users | Retention | H |
| 34 | Cohort retention matrix | Retention | H |
| 35 | DAU/MAU stickiness | Engagement | M |
| 36 | Growth accounting: new, retained, resurrected, churned | Growth | H |
| 37 | Repeat-purchase rate within 30 days | Retention | M |
| 38 | Org chart with depth and path | Recursive CTE | H |
| 39 | Daily signups with a date spine | Recursive CTE | M |
| 40 | Bill of materials cost roll-up | Recursive CTE | H |
| 41 | Pivot monthly revenue into columns | Pivot | M |
| 42 | Unpivot store prices | Unpivot | M |
| 43 | Distinct products sold per date | STRING_AGG | M |
| 44 | Latest record per key with tie-breaker | Dedup | M |
| 45 | Apply a CDC log to get current state | CDC | H |
| 46 | Build SCD Type 2 from daily snapshots | SCD2 | H |
| 47 | Point-in-time FX conversion (as-of join) | As-of join | H |
| 48 | One-query data quality report | Data quality | M |
| 49 | Merge overlapping meetings per room | Intervals | H |
| 50 | Users with overlapping subscriptions | Intervals | H |

Datasets live in `datasets/` (`hr`, `ecommerce`, `events`, `social`, `subscriptions`, `cdc`, `quality`, `misc`). Each file's header lists the traps baked into it.

---

## Study plan

**Pass 1: learn the patterns (about 2 weeks, 4 to 5 problems a day).** Work in topic order. No timer. If you are stuck for 20 minutes, read the solution, close it, and rewrite the query from memory the next day.

**Pass 2: interview simulation (about 1 week).** Reset your files (keep your pass-1 answers in a branch or copy) and use `python3 run.py --random any`. Time-box 15 minutes for medium and 25 for hard. Talk out loud: restate the problem, ask about ties/NULLs/time zones, sketch CTEs before writing, then test edge cases with `--scratch`.

**Final 2 days:** redo every problem you failed or needed the solution for, plus 24, 28, 36, 46, and 47, which are the most common "senior DE" signals.

### Is 50 enough?

Yes, if you do both passes. Top-tier DE SQL rounds pull from about a dozen patterns, and every one of them is here at least twice. Doing 150 problems once is weaker preparation than doing these 50 twice under a timer. If you finish early, the best next step is not more of the same; it is explaining query plans and costs (partition pruning, join strategies, clustering, incremental models), which often comes up right after the SQL question.

---

## Pattern cheat sheet

**Top N per group (ties matter: pick the right function)**

```sql
SELECT * FROM t
QUALIFY DENSE_RANK() OVER (PARTITION BY grp ORDER BY metric DESC) <= 3;
-- ROW_NUMBER: exactly N rows   RANK: ties, gaps after   DENSE_RANK: ties, no gaps
```

**Gaps and islands (consecutive days / ids)**

```sql
SELECT user_id, MIN(d) AS start_d, MAX(d) AS end_d, COUNT(*) AS len
FROM (SELECT user_id, d, d - CAST(ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY d) AS INTEGER) AS k
      FROM (SELECT DISTINCT user_id, CAST(ts AS DATE) AS d FROM logins))
GROUP BY user_id, k;
```

**Sessionization / interval merging (flag + running sum)**

```sql
WITH f AS (
  SELECT *, CASE WHEN ts - LAG(ts) OVER w > INTERVAL 30 MINUTE OR LAG(ts) OVER w IS NULL
                 THEN 1 ELSE 0 END AS is_new
  FROM events WINDOW w AS (PARTITION BY user_id ORDER BY ts))
SELECT *, SUM(is_new) OVER (PARTITION BY user_id ORDER BY ts ROWS UNBOUNDED PRECEDING) AS session_id
FROM f;
-- Merging intervals: compare start to the running MAX(end) of earlier rows, not LAG(end).
```

**Date spine (fill missing days)**

```sql
WITH spine AS (SELECT CAST(d AS DATE) AS d
               FROM generate_series(DATE '2025-01-01', DATE '2025-01-31', INTERVAL 1 DAY) t(d))
SELECT s.d, COALESCE(SUM(x.amount), 0) AS amount
FROM spine s LEFT JOIN facts x ON x.day = s.d
GROUP BY s.d;   -- COUNT(x.id), never COUNT(*), after a LEFT JOIN
```

**Latest row per key / CDC apply**

```sql
SELECT * FROM changes
QUALIFY ROW_NUMBER() OVER (PARTITION BY id ORDER BY lsn DESC) = 1;   -- then drop op = 'D'
```

**SCD Type 2 from snapshots**

```sql
WITH c AS (SELECT *, LAG(attr) OVER (PARTITION BY id ORDER BY snap_date) AS prev FROM snapshots)
SELECT id, attr, snap_date AS valid_from,
       LEAD(snap_date) OVER (PARTITION BY id ORDER BY snap_date) AS valid_to
FROM c WHERE prev IS NULL OR prev <> attr;
```

**As-of join (value in effect at event time)**

```sql
SELECT e.*, r.rate
FROM events e LEFT JOIN rates r ON r.key = e.key AND r.effective_ts <= e.ts
QUALIFY ROW_NUMBER() OVER (PARTITION BY e.event_id ORDER BY r.effective_ts DESC) = 1;
```

**Interval overlap test**

```sql
a.start <= b.end AND b.start <= a.end        -- inclusive ends; COALESCE open ends first
```

**Habits interviewers look for**

- `NOT EXISTS` over `NOT IN` (NULLs).
- Half-open time ranges: `ts >= '2025-01-01' AND ts < '2026-01-01'`.
- Deterministic window ordering: add a unique tie-breaker column.
- Aggregate to the right grain before windowing; dedupe before counting.
- Say your assumptions out loud: ties, NULLs, time zones, late-arriving data.

---

## Dialect notes (DuckDB vs Snowflake)

| Concept | DuckDB | Snowflake |
|---|---|---|
| Truncate | `date_trunc('month', ts)` | `DATE_TRUNC('month', ts)` |
| Date diff | `date_diff('day', a, b)` | `DATEDIFF('day', a, b)` |
| Conditional count | `COUNT(*) FILTER (WHERE x)` | `COUNT_IF(x)` |
| String agg | `STRING_AGG(x, ',' ORDER BY x)` | `LISTAGG(x, ',') WITHIN GROUP (ORDER BY x)` |
| Integer division | `a // b` (`/` is float) | `TRUNC(a / b)` (`/` is float) |
| As-of join | `ASOF LEFT JOIN ... ON k = k AND t >= t` | `ASOF JOIN ... MATCH_CONDITION (t >= t) ON k = k` |
| Series | `generate_series(a, b, INTERVAL 1 DAY)` | `TABLE(GENERATOR(ROWCOUNT => n))` + `DATEADD` |

---

## Adding your own problems

1. Add tables or rows to a file in `datasets/`.
2. Add a `Problem(...)` entry in `catalog.py`.
3. Create `problems/NN_slug.sql` (copy an existing header) and `solutions/NN_slug.sql`.
4. Work out the expected answer by hand, then run `python3 run.py NN --solution` and confirm it matches.
5. Freeze it: `python3 run.py --freeze NN` writes `expected/NN.json`.
