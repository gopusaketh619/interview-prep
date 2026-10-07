-- 10. Percentage of immediate first orders: reference solution
--
-- Approach: keep each customer's first order with QUALIFY ROW_NUMBER() = 1, then the average of a
--           0/1 flag is the fraction. QUALIFY works in DuckDB, Snowflake, BigQuery, and Databricks;
--           in Postgres, wrap the window in a subquery instead.
-- Traps:
--   * The guest order (NULL customer_id) would form its own "customer" group and skew the ratio.
--   * Integer division: 100 * SUM(flag) / COUNT(*) truncates in Postgres/SQL Server. Multiply by
--     100.0 or use AVG on the flag.

WITH first_orders AS (
    SELECT customer_id, order_date, preferred_delivery_date
    FROM orders
    WHERE customer_id IS NOT NULL
    QUALIFY ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date, order_id) = 1
)
SELECT ROUND(100.0 * AVG(CASE WHEN order_date = preferred_delivery_date THEN 1 ELSE 0 END), 2)
       AS immediate_percentage
FROM first_orders;
