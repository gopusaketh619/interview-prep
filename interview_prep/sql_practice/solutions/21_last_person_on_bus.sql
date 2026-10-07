-- 21. Last person to fit on the bus: reference solution
--
-- Approach: running SUM(weight) in turn order; the answer is the last row whose running total is
--           still <= 1000. Running totals only grow, so "last row under the cap" is well defined.
-- Traps:
--   * Ordering by person_id instead of turn.
--   * Greedily skipping heavy people and letting later light ones on (not what the prompt says).

WITH boarding AS (
    SELECT person_name, turn,
           SUM(weight) OVER (ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
               AS total_weight
    FROM queue
)
SELECT person_name
FROM boarding
WHERE total_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
