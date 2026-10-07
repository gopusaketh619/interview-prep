-- 33. Month-over-month retained users: reference solution
--
-- Approach: reduce logins to distinct (user, month), then self-join each month to the same user's
--           previous month.
-- Traps:
--   * Joining raw logins multiplies rows (user 1 has many January logins); dedupe to months first.
--   * Comparing month numbers (MONTH(x) = MONTH(y) - 1) breaks at January vs December. Join on
--     month - INTERVAL 1 MONTH using truncated dates.
-- Alternative: EXISTS (SELECT 1 FROM user_months p WHERE p.user_id = c.user_id AND p.month = ...).

WITH user_months AS (
    SELECT DISTINCT user_id, CAST(date_trunc('month', login_ts) AS DATE) AS month
    FROM logins
)
SELECT strftime(c.month, '%Y-%m') AS month,
       COUNT(*)                   AS retained_users
FROM user_months c
JOIN user_months p
  ON p.user_id = c.user_id
 AND p.month = c.month - INTERVAL 1 MONTH
GROUP BY c.month
ORDER BY c.month;
