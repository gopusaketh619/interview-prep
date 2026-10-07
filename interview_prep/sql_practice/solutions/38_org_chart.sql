-- 38. Org chart with depth and path: reference solution
--
-- Approach: recursive CTE. The anchor selects the root (manager_id IS NULL); the recursive member
--           joins employees whose manager is already in the tree, carrying depth + 1 and the path.
-- Traps:
--   * Self-joining a fixed number of times (e, m1, m2, m3) only handles a known maximum depth.
--   * Cycles in dirty data loop forever. Guard with `WHERE t.depth < 20` or by checking that the
--     path does not already contain the employee.
-- Follow-up interviewers ask: "count all direct + indirect reports per manager" -> anchor every
--   employee as a root, recurse down, then GROUP BY root.

WITH RECURSIVE tree AS (
    SELECT emp_id, name, 0 AS depth, CAST(name AS VARCHAR) AS path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.emp_id, e.name, t.depth + 1, t.path || ' > ' || e.name
    FROM employees e
    JOIN tree t ON e.manager_id = t.emp_id
)
SELECT name AS employee, depth, path
FROM tree
ORDER BY path;
