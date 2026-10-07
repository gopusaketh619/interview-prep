-- 07. Departments above the company average salary: reference solution
--
-- Approach: compare each department's AVG against a scalar subquery over all employees.
-- Trap: averaging the department averages (an "average of averages") gives 122,500 instead of the
--       true 130,769.23, which wrongly lets Legal (130,000) through. Weighting matters.
-- Alternative: AVG(salary) OVER () as a window in a CTE, then filter.

SELECT d.dept_name,
       ROUND(AVG(e.salary), 2) AS avg_salary
FROM employees e
JOIN departments d ON d.dept_id = e.dept_id
GROUP BY d.dept_name
HAVING AVG(e.salary) > (SELECT AVG(salary) FROM employees);
