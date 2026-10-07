-- 49. Merge overlapping meetings per room: reference solution
--
-- Approach: sort by start. A booking starts a new block when it starts after the MAXIMUM end of
--           every earlier booking in the room. A running SUM of that flag numbers the blocks.
-- Trap: comparing against only the previous row's end (LAG(end_ts)) breaks on nested bookings.
--       Room A's 14:00 meeting follows the 12:30-13:00 one, so LAG says "gap", but 12:00-15:00 is
--       still running. The running MAX of end_ts fixes it.
-- Pattern: this flag + running sum is the same shape as sessionization (problem 28).

WITH ordered AS (
    SELECT room, start_ts, end_ts,
           MAX(end_ts) OVER (
               PARTITION BY room ORDER BY start_ts, end_ts
               ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
           ) AS prev_max_end
    FROM meetings
),
blocks AS (
    SELECT room, start_ts, end_ts,
           SUM(CASE WHEN prev_max_end IS NULL OR start_ts > prev_max_end THEN 1 ELSE 0 END) OVER (
               PARTITION BY room ORDER BY start_ts, end_ts
               ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
           ) AS block_id
    FROM ordered
)
SELECT room, MIN(start_ts) AS start_ts, MAX(end_ts) AS end_ts
FROM blocks
GROUP BY room, block_id;
