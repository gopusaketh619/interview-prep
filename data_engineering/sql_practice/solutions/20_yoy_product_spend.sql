-- 20. Year-over-year spend growth per product: reference solution
--
-- Approach: aggregate to (product, year) and LEFT JOIN each year to the same product's year - 1.
-- Trap: LAG(spend) OVER (PARTITION BY product_id ORDER BY year) compares product 2's 2024 spend
--       against 2022, because 2023 has no row. Joining on `yr - 1` makes the gap explicit.
-- Alternative: LAG plus a check that the lagged year equals year - 1:
--   CASE WHEN LAG(yr) OVER w = yr - 1 THEN LAG(spend) OVER w END

WITH yearly AS (
    SELECT product_id, YEAR(transaction_date) AS yr, SUM(spend) AS spend
    FROM product_spend
    GROUP BY product_id, yr
)
SELECT c.yr          AS year,
       c.product_id,
       c.spend       AS curr_year_spend,
       p.spend       AS prev_year_spend,
       ROUND(100.0 * (c.spend - p.spend) / p.spend, 2) AS yoy_rate
FROM yearly c
LEFT JOIN yearly p
       ON p.product_id = c.product_id
      AND p.yr = c.yr - 1;
