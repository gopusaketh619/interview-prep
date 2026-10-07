-- 03. Products frequently bought together: reference solution
--
-- Approach: dedupe to (order_id, product_id), self-join on order_id with a.product_id < b.product_id
--           so each unordered pair appears once and a product never pairs with itself.
-- Traps:
--   * Order 16 lists Headphones twice. Without the DISTINCT step, Laptop+Headphones counts 5, not 4.
--   * Using `<>` instead of `<` reports every pair twice (A,B and B,A).
-- Scale note: self-joins on large orders explode quadratically; in production you would cap
--             basket size or pre-aggregate per order.

WITH order_products AS (
    SELECT DISTINCT order_id, product_id
    FROM order_items
)
SELECT pa.name AS product_a,
       pb.name AS product_b,
       COUNT(*) AS orders_together
FROM order_products a
JOIN order_products b
  ON a.order_id = b.order_id
 AND a.product_id < b.product_id
JOIN products pa ON pa.product_id = a.product_id
JOIN products pb ON pb.product_id = b.product_id
GROUP BY a.product_id, b.product_id, pa.name, pb.name
HAVING COUNT(*) >= 2
ORDER BY orders_together DESC, a.product_id, b.product_id;
