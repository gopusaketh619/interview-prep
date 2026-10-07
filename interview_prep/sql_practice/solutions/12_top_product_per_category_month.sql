-- 12. Top-selling product per category per month: reference solution
--
-- Approach: aggregate to (month, category, product), then RANK within (month, category) and keep
--           rank 1. RANK (or DENSE_RANK) keeps ties; ROW_NUMBER would silently pick one winner.
-- Traps:
--   * Feb Furniture (Desk 3, Chair 3), Feb Books, and Mar Electronics are ties.
--   * Order 16 lists Headphones on two lines; SUM(quantity) handles that correctly, unlike COUNT(*).
-- Interview tip: always ask "what about ties?" before choosing ROW_NUMBER vs RANK.

WITH monthly AS (
    SELECT strftime(o.order_date, '%Y-%m') AS month,
           p.category,
           p.name AS product,
           SUM(oi.quantity) AS total_quantity
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    JOIN products p     ON p.product_id = oi.product_id
    GROUP BY ALL
)
SELECT month, category, product, total_quantity
FROM monthly
QUALIFY RANK() OVER (PARTITION BY month, category ORDER BY total_quantity DESC) = 1;
