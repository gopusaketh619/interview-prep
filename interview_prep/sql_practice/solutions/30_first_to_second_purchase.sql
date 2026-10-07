-- 30. Average days from first to second order: reference solution
--
-- Approach: number each customer's orders, then LEAD from order 1 to order 2 (or self-join rn 1 to
--           rn 2). Customers with a single order have a NULL gap, which AVG ignores.
-- Traps:
--   * Averaging every consecutive gap instead of only first -> second.
--   * Engine differences in date subtraction: DuckDB DATE - DATE returns days as an integer,
--     Snowflake uses DATEDIFF('day', a, b), Postgres returns an integer, BigQuery DATE_DIFF.
--     date_diff('day', a, b) reads the same in most dialects.

WITH numbered AS (
    SELECT customer_id, order_date,
           LEAD(order_date) OVER (PARTITION BY customer_id ORDER BY order_date, order_id) AS next_date,
           ROW_NUMBER()     OVER (PARTITION BY customer_id ORDER BY order_date, order_id) AS rn
    FROM orders
    WHERE customer_id IS NOT NULL
)
SELECT ROUND(AVG(date_diff('day', order_date, next_date)), 2) AS avg_days_to_second_order
FROM numbered
WHERE rn = 1;
