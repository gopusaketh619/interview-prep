-- 48. One-query data quality report: reference solution
--
-- Approach: one scalar aggregate per check, stacked with UNION ALL. Each branch always returns
--           exactly one row (aggregates without GROUP BY), so zero-failure checks still appear.
-- Traps:
--   * Counting duplicate ROWS (3 + 3 + 5 + 5 = 4 extra) vs duplicate KEYS (3 and 5 = 2). Read the
--     definition; both are valid checks.
--   * `customer_id NOT IN (SELECT customer_id FROM dq_customers)` is fine here only because the
--     customer side has no NULL ids. NOT EXISTS is the safe default.
--   * Orphan and NULL foreign keys are different failures; a LEFT JOIN ... IS NULL check lumps the
--     NULL-FK order in with the orphans unless you exclude it.
-- In production: these map to dbt's unique, not_null, and relationships tests.

SELECT 'duplicate_customer_id' AS check_name, COUNT(*) AS failed_count
FROM (
    SELECT customer_id FROM dq_customers GROUP BY customer_id HAVING COUNT(*) > 1
)
UNION ALL
SELECT 'null_customer_email', COUNT(*) FROM dq_customers WHERE email IS NULL
UNION ALL
SELECT 'orphan_order_customer', COUNT(*)
FROM dq_orders o
WHERE o.customer_id IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM dq_customers c WHERE c.customer_id = o.customer_id)
UNION ALL
SELECT 'null_order_customer', COUNT(*) FROM dq_orders WHERE customer_id IS NULL
UNION ALL
SELECT 'negative_order_amount', COUNT(*) FROM dq_orders WHERE amount < 0;
