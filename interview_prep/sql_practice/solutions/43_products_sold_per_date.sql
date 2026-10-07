-- 43. Distinct products sold per date: reference solution
--
-- Approach: COUNT(DISTINCT) plus an ordered, distinct STRING_AGG.
-- Trap: STRING_AGG without DISTINCT lists 'Mask,Mask' on 2020-06-02.
-- Dialects:
--   Snowflake:  LISTAGG(DISTINCT product, ',') WITHIN GROUP (ORDER BY product)
--   BigQuery:   STRING_AGG(DISTINCT product, ',' ORDER BY product)
--   Postgres:   STRING_AGG(DISTINCT product, ',' ORDER BY product)
--   MySQL:      GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',')

SELECT sell_date,
       COUNT(DISTINCT product)                           AS num_sold,
       STRING_AGG(DISTINCT product, ',' ORDER BY product) AS products
FROM sales_log
GROUP BY sell_date
ORDER BY sell_date;
