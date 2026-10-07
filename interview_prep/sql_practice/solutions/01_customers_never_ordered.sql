-- 01. Customers who never ordered: reference solution
--
-- Approach: anti-join with NOT EXISTS.
-- Trap: `WHERE customer_id NOT IN (SELECT customer_id FROM orders)` returns zero rows here,
--       because the subquery contains a NULL (guest order 13). `x NOT IN (..., NULL)` is never
--       TRUE, only FALSE or UNKNOWN. NOT EXISTS and LEFT JOIN ... IS NULL are NULL-safe.
-- Alternative: LEFT JOIN orders o ON o.customer_id = c.customer_id WHERE o.order_id IS NULL.

SELECT c.customer_id, c.name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);
