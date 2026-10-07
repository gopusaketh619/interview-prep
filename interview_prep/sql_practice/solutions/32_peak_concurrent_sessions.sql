-- 32. Peak concurrent sessions: reference solution
--
-- Approach (sweep line): turn each session into +1 at start and -1 at end, net the deltas per
--           timestamp, and take a running SUM. The running value is the live count from that
--           timestamp until the next one.
-- Traps:
--   * Treating end_ts as inclusive counts 4 at 11:00 (session 1 ending, session 3 starting).
--     Netting deltas per timestamp first handles the boundary correctly.
--   * The self-join version (count sessions where s2.start <= s1.start < s2.end) works but is
--     O(n^2); the sweep is O(n log n) and the one to mention in a DE interview.

WITH deltas AS (
    SELECT start_ts AS ts, 1 AS delta FROM user_sessions
    UNION ALL
    SELECT end_ts AS ts, -1 AS delta FROM user_sessions
),
net AS (
    SELECT ts, SUM(delta) AS delta
    FROM deltas
    GROUP BY ts
),
live AS (
    SELECT ts, SUM(delta) OVER (ORDER BY ts ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS live
    FROM net
)
SELECT live AS peak_concurrent, ts AS peak_start_ts
FROM live
ORDER BY live DESC, ts
LIMIT 1;
