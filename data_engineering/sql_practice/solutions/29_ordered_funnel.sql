-- 29. Ordered conversion funnel within 7 days: reference solution
--
-- Approach: chain the steps with time-bounded joins. Each later step joins to the previous step's
--           qualifying rows, carrying the view timestamp along so the 7-day window is anchored on it.
-- Traps:
--   * Counting users who have each event type at all (COUNT DISTINCT per type) ignores order:
--     user 3 carts before viewing, user 2 purchases 11 days after the view.
--   * Anchoring the purchase window on the cart time instead of the view time.
-- Scale note: on big event tables, pre-filter to the three event types and a date range first;
--             Snowflake MATCH_RECOGNIZE can express ordered funnels without self-joins.

WITH views AS (
    SELECT user_id, event_ts AS view_ts
    FROM events
    WHERE event_type = 'view'
),
carts AS (
    SELECT v.user_id, v.view_ts, e.event_ts AS cart_ts
    FROM views v
    JOIN events e
      ON e.user_id = v.user_id
     AND e.event_type = 'add_to_cart'
     AND e.event_ts > v.view_ts
     AND e.event_ts <= v.view_ts + INTERVAL 7 DAY
),
purchases AS (
    SELECT DISTINCT c.user_id
    FROM carts c
    JOIN events e
      ON e.user_id = c.user_id
     AND e.event_type = 'purchase'
     AND e.event_ts > c.cart_ts
     AND e.event_ts <= c.view_ts + INTERVAL 7 DAY
)
SELECT 1 AS step_order, 'view' AS step, COUNT(DISTINCT user_id) AS users FROM views
UNION ALL
SELECT 2, 'add_to_cart', COUNT(DISTINCT user_id) FROM carts
UNION ALL
SELECT 3, 'purchase', COUNT(*) FROM purchases
ORDER BY step_order;
