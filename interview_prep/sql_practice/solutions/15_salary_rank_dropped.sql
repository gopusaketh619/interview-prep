-- 15. Employees whose salary rank dropped: reference solution
--
-- Approach: rank once with PARTITION BY (dept, year), then pivot the two years side by side with
--           conditional aggregation and compare.
-- Traps:
--   * Partitioning by department only (not year) ranks 2024 and 2025 salaries against each other.
--   * Leo has no 2024 row; MAX(...) FILTER returns NULL for him and NULL > x is not TRUE, so he
--     drops out, which is what the prompt asks for.
-- Alternative: two CTEs (one per year) joined on emp_id.

WITH ranked AS (
    SELECT h.emp_id, h.year, e.name, e.dept_id,
           DENSE_RANK() OVER (PARTITION BY e.dept_id, h.year ORDER BY h.salary DESC) AS rnk
    FROM salary_history h
    JOIN employees e ON e.emp_id = h.emp_id
),
by_year AS (
    SELECT emp_id, name, dept_id,
           MAX(rnk) FILTER (WHERE year = 2024) AS rank_2024,
           MAX(rnk) FILTER (WHERE year = 2025) AS rank_2025
    FROM ranked
    GROUP BY emp_id, name, dept_id
)
SELECT d.dept_name, b.name AS employee, b.rank_2024, b.rank_2025
FROM by_year b
JOIN departments d ON d.dept_id = b.dept_id
WHERE b.rank_2025 > b.rank_2024;
