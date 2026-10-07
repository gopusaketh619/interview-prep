-- 35. DAU/MAU stickiness: reference solution
--
-- Approach: one row per (user, day). Per month, COUNT(*) is the sum of daily actives, and dividing
--           by the days in the month (day(last_day(...))) gives the calendar-day average.
-- Traps:
--   * AVG of a per-day count only averages days that had logins (inflating DAU on quiet months).
--   * Counting logins instead of distinct (user, day) pairs: user 1 logs in twice on 01-02.
--   * Rounding avg_dau before dividing by MAU changes stickiness in the second decimal.

WITH user_days AS (
    SELECT DISTINCT user_id, CAST(login_ts AS DATE) AS d
    FROM logins
),
monthly AS (
    SELECT date_trunc('month', d)            AS month_start,
           COUNT(*)                          AS user_days,
           COUNT(DISTINCT user_id)           AS mau,
           MAX(day(last_day(d)))             AS days_in_month
    FROM user_days
    GROUP BY month_start
)
SELECT strftime(month_start, '%Y-%m')                          AS month,
       ROUND(user_days / days_in_month, 2)                     AS avg_dau,
       mau,
       ROUND(100.0 * user_days / days_in_month / mau, 2)       AS stickiness_pct
FROM monthly
ORDER BY month;
