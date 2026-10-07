-- 34. Cohort retention matrix: reference solution
--
-- Approach: cohort per user from users.signup_date, cohort sizes computed from users (not logins),
--           distinct active months from logins, then month_number = months between the two.
-- Traps:
--   * Computing cohort_size from logins drops user 8 (signed up, never logged in) and inflates
--     January retention from 80% to 100%.
--   * Using the first login month as the cohort instead of the signup month.
--   * Counting raw logins instead of distinct users per month.
-- Presentation: to show a classic triangle, pivot month_number into columns (see problem 41).

WITH cohorts AS (
    SELECT user_id, CAST(date_trunc('month', signup_date) AS DATE) AS cohort
    FROM users
),
cohort_sizes AS (
    SELECT cohort, COUNT(*) AS cohort_size
    FROM cohorts
    GROUP BY cohort
),
active_months AS (
    SELECT DISTINCT user_id, CAST(date_trunc('month', login_ts) AS DATE) AS month
    FROM logins
)
SELECT strftime(c.cohort, '%Y-%m')          AS cohort_month,
       date_diff('month', c.cohort, a.month) AS month_number,
       COUNT(*)                              AS active_users,
       s.cohort_size,
       ROUND(100.0 * COUNT(*) / s.cohort_size, 2) AS retention_pct
FROM cohorts c
JOIN active_months a ON a.user_id = c.user_id
JOIN cohort_sizes s  ON s.cohort = c.cohort
GROUP BY c.cohort, a.month, s.cohort_size;
