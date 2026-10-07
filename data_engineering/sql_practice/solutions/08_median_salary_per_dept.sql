-- 08. Median salary per department: reference solution
--
-- Approach: number rows within each department and count them, then average the middle row(s).
--           For n rows the middle positions are (n + 1) // 2 and (n + 2) // 2, which coincide when
--           n is odd and are the two middle rows when n is even.
-- Traps:
--   * DuckDB's `/` is float division even for integers (unlike Postgres); use `//` for integer
--     division, or FLOOR / CEIL.
--   * Picking only one middle row gives 90,000 for Sales instead of (90,000 + 100,000) / 2.
-- Check yourself: MEDIAN(salary) gives the same answer; use it once you're allowed to.

WITH ordered AS (
    SELECT dept_id, salary,
           ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary) AS rn,
           COUNT(*)     OVER (PARTITION BY dept_id)                 AS n
    FROM employees
)
SELECT d.dept_name, AVG(o.salary) AS median_salary
FROM ordered o
JOIN departments d ON d.dept_id = o.dept_id
WHERE o.rn IN ((o.n + 1) // 2, (o.n + 2) // 2)
GROUP BY d.dept_name;
