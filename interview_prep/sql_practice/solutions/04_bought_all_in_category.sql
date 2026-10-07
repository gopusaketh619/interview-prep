-- 04. Customers who bought every Electronics product: reference solution
--
-- Approach (relational division by counting): count DISTINCT Electronics products per customer and
--           compare against the total number of Electronics products, computed from `products`.
-- Traps:
--   * COUNT(product_id) instead of COUNT(DISTINCT product_id): customer 2 has three Electronics
--     lines (Phone, Headphones, Headphones) but only two distinct products.
--   * Hard-coding `= 3` breaks as soon as the catalog changes.
-- Alternative (double NOT EXISTS): "there is no Electronics product this customer did not buy".

SELECT o.customer_id
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p     ON p.product_id = oi.product_id
WHERE p.category = 'Electronics'
  AND o.customer_id IS NOT NULL
GROUP BY o.customer_id
HAVING COUNT(DISTINCT oi.product_id) = (
    SELECT COUNT(*) FROM products WHERE category = 'Electronics'
);
