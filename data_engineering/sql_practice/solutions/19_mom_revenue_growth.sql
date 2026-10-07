-- 19. Month-over-month revenue growth: reference solution
--
-- Approach: aggregate to months, then LAG(revenue) over month order.
-- Traps:
--   * LAG looks at the previous ROW, not the previous calendar month. If a month had no orders,
--     LAG would compare against two months ago. Join a month spine first when gaps are possible
--     (see problem 18 and 20).
--   * Guard the division with NULLIF(prev, 0) so a zero month does not raise an error.
--   * Integer division in some engines: multiply by 100.0, not 100.

WITH monthly AS (
    SELECT strftime(o.order_date, '%Y-%m') AS month,
           SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    GROUP BY month
),
with_prev AS (
    SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue
    FROM monthly
)
SELECT month, revenue, prev_month_revenue,
       ROUND(100.0 * (revenue - prev_month_revenue) / NULLIF(prev_month_revenue, 0), 2) AS growth_pct
FROM with_prev
ORDER BY month;
