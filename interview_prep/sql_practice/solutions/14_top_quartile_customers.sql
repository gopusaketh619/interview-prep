-- 14. Top-quartile customers by spend: reference solution
--
-- Approach: aggregate spend per customer, then NTILE(4) over spend DESC and keep bucket 1.
-- Know this: NTILE splits rows as evenly as possible, giving the extra rows to the first buckets.
--            6 customers -> bucket sizes 2, 2, 1, 1. So "top 25%" here is 2 of 6 customers.
-- Alternatives:
--   * PERCENT_RANK() OVER (ORDER BY total_spend DESC) < 0.25 -> handles ties consistently.
--   * CUME_DIST() <= 0.25 -> "share of customers at or above this spend".
--   Ask the interviewer which definition they want; they give different answers with ties.

WITH spend AS (
    SELECT o.customer_id, SUM(oi.quantity * oi.unit_price) AS total_spend
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.customer_id IS NOT NULL
    GROUP BY o.customer_id
)
SELECT customer_id, total_spend
FROM spend
QUALIFY NTILE(4) OVER (ORDER BY total_spend DESC, customer_id) = 1;
