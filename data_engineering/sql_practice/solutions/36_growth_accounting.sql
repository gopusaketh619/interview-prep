-- 36. Growth accounting: reference solution
--
-- Approach: build a grid of (user, month) for every month on or after the user's first month, then
--           look up "active now" and "active last month" with LEFT JOINs and classify with CASE.
-- Traps:
--   * Churned users have no login in the month they churn, so they only show up if you generate the
--     grid; a query that starts FROM logins can never produce them.
--   * Distinguishing resurrected from new needs the user's first month, not just last month.
--   * The grid uses months that appear in the data. If a month could have zero logins overall, use
--     a calendar spine instead (problem 39).
-- Sanity check: MAU(m) = new + retained + resurrected, and MAU(m-1) = retained + churned.

WITH user_months AS (
    SELECT DISTINCT user_id, CAST(date_trunc('month', login_ts) AS DATE) AS month
    FROM logins
),
months AS (
    SELECT DISTINCT month FROM user_months
),
first_month AS (
    SELECT user_id, MIN(month) AS first_month
    FROM user_months
    GROUP BY user_id
),
classified AS (
    SELECT m.month,
           CASE
               WHEN cur.user_id IS NOT NULL AND m.month = f.first_month THEN 'new'
               WHEN cur.user_id IS NOT NULL AND prev.user_id IS NOT NULL THEN 'retained'
               WHEN cur.user_id IS NOT NULL                              THEN 'resurrected'
               WHEN prev.user_id IS NOT NULL                             THEN 'churned'
           END AS status
    FROM first_month f
    JOIN months m ON m.month >= f.first_month
    LEFT JOIN user_months cur
           ON cur.user_id = f.user_id AND cur.month = m.month
    LEFT JOIN user_months prev
           ON prev.user_id = f.user_id AND prev.month = m.month - INTERVAL 1 MONTH
)
SELECT strftime(month, '%Y-%m') AS month, status, COUNT(*) AS users
FROM classified
WHERE status IS NOT NULL
GROUP BY ALL;
