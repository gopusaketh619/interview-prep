-- 39. Daily signups with a date spine: reference solution
--
-- Approach: recursive CTE that adds one day until the end date, LEFT JOIN users onto it, and count
--           a column from the right-hand table.
-- Traps:
--   * COUNT(*) after a LEFT JOIN counts the spine row itself, so empty days show 1 instead of 0.
--     COUNT(u.user_id) counts only matches.
--   * Putting a filter on `u` in WHERE turns the LEFT JOIN back into an INNER JOIN.
-- Other engines: Snowflake TABLE(GENERATOR(ROWCOUNT => n)) + DATEADD; BigQuery GENERATE_DATE_ARRAY;
--                Postgres generate_series(date, date, interval '1 day').

WITH RECURSIVE spine(d) AS (
    SELECT DATE '2025-01-01'
    UNION ALL
    SELECT CAST(d + INTERVAL 1 DAY AS DATE)
    FROM spine
    WHERE d < DATE '2025-01-10'
)
SELECT s.d AS signup_date, COUNT(u.user_id) AS signups
FROM spine s
LEFT JOIN users u ON u.signup_date = s.d
GROUP BY s.d
ORDER BY s.d;
