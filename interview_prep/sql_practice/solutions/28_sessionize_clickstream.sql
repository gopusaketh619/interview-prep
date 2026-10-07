-- 28. Sessionize a clickstream: reference solution
--
-- Approach (flag + running sum, the standard sessionization pattern):
--   1. LAG the previous event time per user; flag 1 when there is none or the gap is > 30 minutes.
--   2. A running SUM of the flag numbers the sessions.
--   3. Aggregate per (user, session).
-- Traps:
--   * `>=` instead of `>` splits user 1's 10:10 -> 10:40 into two sessions.
--   * Forgetting PARTITION BY user_id in the LAG lets one user's events continue another's session.

WITH flagged AS (
    SELECT user_id, event_ts,
           CASE
               WHEN LAG(event_ts) OVER w IS NULL THEN 1
               WHEN event_ts - LAG(event_ts) OVER w > INTERVAL 30 MINUTE THEN 1
               ELSE 0
           END AS is_new_session
    FROM events
    WINDOW w AS (PARTITION BY user_id ORDER BY event_ts)
),
numbered AS (
    SELECT user_id, event_ts,
           SUM(is_new_session) OVER (
               PARTITION BY user_id ORDER BY event_ts
               ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
           ) AS session_id
    FROM flagged
)
SELECT user_id, session_id,
       MIN(event_ts) AS session_start,
       MAX(event_ts) AS session_end,
       COUNT(*)      AS event_count
FROM numbered
GROUP BY user_id, session_id;
