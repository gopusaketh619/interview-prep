-- 06. Monthly transactions by country: reference solution
--
-- Approach: one GROUP BY with conditional aggregates. FILTER (WHERE ...) is supported by DuckDB,
--           Postgres, and Snowflake (COUNT_IF / SUM(IFF(...)) there); SUM(CASE WHEN ...) works everywhere.
-- Traps:
--   * GROUP BY keeps NULL as a group, but an INNER JOIN to a country dimension would drop it.
--   * SUM over zero matching rows is NULL; wrap it in COALESCE to report 0.

SELECT strftime(trans_date, '%Y-%m')                                AS month,
       country,
       COUNT(*)                                                     AS trans_count,
       COUNT(*) FILTER (WHERE state = 'approved')                   AS approved_count,
       SUM(amount)                                                  AS trans_total_amount,
       COALESCE(SUM(amount) FILTER (WHERE state = 'approved'), 0)   AS approved_total_amount
FROM transactions
GROUP BY month, country;
