-- 40. Bill of materials cost roll-up: reference solution
--
-- Approach: explode each top-level product down the tree with a recursive CTE, multiplying
--           quantities along the path. Then price the leaves (parts with a unit_cost) and sum.
-- Traps:
--   * Not multiplying quantities through levels: a Bike has 2 Wheels x 32 Spokes = 64 spokes.
--   * Summing assembly rows as well as leaves double counts (assemblies have NULL cost here, but in
--     real data they may carry a stale rolled-up cost).
-- Check: Wheel = 32 * 0.5 + 15 + 20 = 51, Bike = 2 * 51 + 120 = 222, Scooter = 2 * 51 + 40 = 142.

WITH RECURSIVE explode AS (
    SELECT b.parent_id AS root_id, b.child_id, CAST(b.qty AS DECIMAL(18, 4)) AS qty
    FROM bom b
    WHERE NOT EXISTS (SELECT 1 FROM bom c WHERE c.child_id = b.parent_id)

    UNION ALL

    SELECT e.root_id, b.child_id, e.qty * b.qty
    FROM explode e
    JOIN bom b ON b.parent_id = e.child_id
)
SELECT r.name AS product, SUM(e.qty * p.unit_cost) AS total_cost
FROM explode e
JOIN parts p ON p.part_id = e.child_id
JOIN parts r ON r.part_id = e.root_id
WHERE p.unit_cost IS NOT NULL
GROUP BY r.name;
