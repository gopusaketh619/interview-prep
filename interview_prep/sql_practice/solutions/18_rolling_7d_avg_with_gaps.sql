-- 18. 7-day rolling average with missing days: reference solution
--
-- Approach: build a date spine with generate_series, LEFT JOIN the sales onto it (COALESCE to 0),
--           then a ROWS window of 6 preceding rows. Because the spine has exactly one row per day,
--           6 preceding rows = 6 preceding calendar days.
-- Traps:
--   * ROWS BETWEEN 6 PRECEDING directly on daily_sales spans 9 calendar days on 01-10, because
--     three days are missing, and missing days are not averaged in as 0.
--   * RANGE BETWEEN INTERVAL 6 DAY PRECEDING on the raw table gets the window right but still
--     averages only the days that have rows (it ignores the zero days).
-- Snowflake equivalent of the spine: GENERATOR + DATEADD, or a calendar dimension table.

WITH bounds AS (
    SELECT MIN(sale_date) AS lo, MAX(sale_date) AS hi FROM daily_sales
),
spine AS (
    SELECT CAST(d AS DATE) AS sale_date
    FROM bounds, generate_series(lo, hi, INTERVAL 1 DAY) AS t(d)
),
filled AS (
    SELECT s.sale_date, COALESCE(ds.revenue, 0) AS revenue
    FROM spine s
    LEFT JOIN daily_sales ds ON ds.sale_date = s.sale_date
)
SELECT sale_date, revenue,
       ROUND(AVG(revenue) OVER (ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2)
           AS rolling_7d_avg
FROM filled
ORDER BY sale_date;
