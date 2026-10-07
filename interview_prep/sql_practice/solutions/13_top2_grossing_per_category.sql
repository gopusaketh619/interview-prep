-- 13. Top 2 grossing products per category: reference solution
--
-- Approach: filter to Q1 with a half-open date range, aggregate per product, rank within category.
-- Traps:
--   * Using products.price instead of order_items.unit_price ignores discounts (order 7 Laptop at
--     1100, order 12 Phone at 750) and overstates revenue.
--   * Filtering after the window (in an outer query) instead of before the aggregation would rank
--     on all-time revenue.

WITH q1 AS (
    SELECT p.category, p.name AS product,
           SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    JOIN products p     ON p.product_id = oi.product_id
    WHERE o.order_date >= DATE '2025-01-01'
      AND o.order_date <  DATE '2025-04-01'
    GROUP BY p.category, p.name
)
SELECT category, product, revenue
FROM q1
QUALIFY RANK() OVER (PARTITION BY category ORDER BY revenue DESC) <= 2;
