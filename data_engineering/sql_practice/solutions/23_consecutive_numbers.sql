-- 23. Numbers appearing 3+ times consecutively: reference solution
--
-- Approach (the classic islands trick): ROW_NUMBER over everything minus ROW_NUMBER within the
--           value is constant across a run of the same value. Group by (num, difference).
-- Trap: the textbook self-join `l2.id = l1.id + 1 AND l3.id = l1.id + 2` assumes ids have no gaps.
--       id 7 is missing, so the run of 2s at ids 6, 8, 9 is missed.
-- Alternative: LAG(num, 1) and LAG(num, 2) over id order, then num = both lags.

WITH islands AS (
    SELECT num,
           ROW_NUMBER() OVER (ORDER BY id)
         - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
    FROM logs
)
SELECT DISTINCT num AS consecutive_num
FROM islands
GROUP BY num, grp
HAVING COUNT(*) >= 3;
