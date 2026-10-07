-- 26. Collapse ids into continuous ranges: reference solution
--
-- Approach: the purest form of gaps and islands. log_id - ROW_NUMBER() is constant within a run.
-- Alternative: flag a new island when log_id <> LAG(log_id) + 1, then a running SUM of the flag
--              gives an island number. That version generalizes to "gap > N" rules (see problem 28).

WITH islands AS (
    SELECT log_id, log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
    FROM log_ids
)
SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM islands
GROUP BY grp;
