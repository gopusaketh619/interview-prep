-- 17. Running revenue that resets each month: reference solution
--
-- Approach: aggregate to one row per order first, then two SUM() OVER windows. The "reset" is
--           just adding the month to PARTITION BY.
-- Traps:
--   * Windowing over order_items rows (before aggregating) produces one row per line item.
--   * With ORDER BY but no frame, the default frame is RANGE UNBOUNDED PRECEDING, which lumps
--     together rows with equal ORDER BY values. Spelling out ROWS BETWEEN ... and a unique
--     ORDER BY (date, order_id) keeps running totals row-by-row.

WITH order_revenue AS (
    SELECT o.customer_id, o.order_id, o.order_date,
           SUM(oi.quantity * oi.unit_price) AS order_revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.customer_id IS NOT NULL
    GROUP BY o.customer_id, o.order_id, o.order_date
)
SELECT customer_id, order_id, order_date, order_revenue,
       SUM(order_revenue) OVER (
           PARTITION BY customer_id
           ORDER BY order_date, order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total,
       SUM(order_revenue) OVER (
           PARTITION BY customer_id, date_trunc('month', order_date)
           ORDER BY order_date, order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_month_total
FROM order_revenue
ORDER BY customer_id, order_date, order_id;
