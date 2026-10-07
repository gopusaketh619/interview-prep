-- 02. Second-highest salary per department: reference solution
--
-- Approach: DENSE_RANK salaries per department, then LEFT JOIN rank 2 back onto departments
--           so departments without a second salary still produce a row (with NULL).
-- Traps:
--   * ROW_NUMBER or RANK treats Marketing's tied 95000 salaries as #1 and #2, returning 95000.
--   * Filtering `rnk = 2` in WHERE after the join silently drops Marketing, Legal, and Research.
--     The filter belongs in the ON clause of the LEFT JOIN.
--   * Carol and Dan tie at 150000 in Engineering; MAX() collapses duplicates at rank 2.

WITH ranked AS (
    SELECT dept_id, salary,
           DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT d.dept_name, MAX(r.salary) AS second_highest_salary
FROM departments d
LEFT JOIN ranked r
       ON r.dept_id = d.dept_id
      AND r.rnk = 2
GROUP BY d.dept_name;
