-- 37. Repeat-purchase rate within 30 days: reference solution
--
-- Approach: LAG the previous order date per customer, reduce to one boolean per customer with
--           BOOL_OR, then take the share of TRUE.
-- Traps:
--   * Dividing by customers with 2+ orders instead of all ordering customers (Hana has one order and
--     belongs in the denominator).
--   * Counting gaps instead of customers: customer 1 has two qualifying gaps but counts once.
-- Portability: BOOL_OR is Postgres/DuckDB; Snowflake has BOOLOR_AGG; MAX(CASE ... THEN 1 ELSE 0)
--              works everywhere.

WITH gaps AS (
    SELECT customer_id,
           date_diff('day',
                     LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date, order_id),
                     order_date) AS gap_days
    FROM orders
    WHERE customer_id IS NOT NULL
),
per_customer AS (
    SELECT customer_id, COALESCE(BOOL_OR(gap_days <= 30), FALSE) AS fast_repeater
    FROM gaps
    GROUP BY customer_id
)
SELECT ROUND(100.0 * COUNT(*) FILTER (WHERE fast_repeater) / COUNT(*), 2) AS repeat_rate_pct
FROM per_customer;
