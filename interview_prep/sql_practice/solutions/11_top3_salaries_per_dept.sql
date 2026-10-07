-- 11. Top 3 distinct salaries per department: reference solution
--
-- Approach: DENSE_RANK assigns the same rank to ties and does not skip numbers, so rank <= 3
--           means "within the top 3 distinct salaries".
-- Know the difference (salaries 250, 180, 150, 150, 120):
--   ROW_NUMBER -> 1, 2, 3, 4, 5   (arbitrary tie-break; drops Dan)
--   RANK       -> 1, 2, 3, 3, 5   (gaps after ties)
--   DENSE_RANK -> 1, 2, 3, 3, 4   (no gaps; what "distinct salaries" means)

SELECT d.dept_name, e.name AS employee, e.salary
FROM employees e
JOIN departments d ON d.dept_id = e.dept_id
QUALIFY DENSE_RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) <= 3;
