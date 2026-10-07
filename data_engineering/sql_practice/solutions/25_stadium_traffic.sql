-- 25. 3+ consecutive high-traffic rows: reference solution
--
-- Approach: keep only rows with people >= 100, then id - ROW_NUMBER() is constant within each run
--           of consecutive ids. Keep runs whose size (a window COUNT) is >= 3.
-- Traps:
--   * The LEAD/LAG approach (check prev2/prev1/next1/next2) works but needs three overlapping cases
--     to catch the first, middle, and last rows of a run. Easy to miss one under time pressure.
--   * Runs of exactly 2 (ids 2-3 and 10-11) must be excluded.

WITH busy AS (
    SELECT id, visit_date, people,
           id - ROW_NUMBER() OVER (ORDER BY id) AS run_key
    FROM stadium
    WHERE people >= 100
)
SELECT id, visit_date, people
FROM busy
QUALIFY COUNT(*) OVER (PARTITION BY run_key) >= 3
ORDER BY visit_date;
