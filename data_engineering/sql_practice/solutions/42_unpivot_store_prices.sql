-- 42. Unpivot store prices: reference solution
--
-- Approach: one SELECT per column, glued with UNION ALL, each filtering out NULLs.
-- Notes:
--   * UNION (without ALL) would also work here but pays for a needless dedupe sort.
--   * DuckDB / Snowflake / Databricks UNPIVOT drops NULLs by default:
--       UNPIVOT products_wide ON store1, store2, store3 INTO NAME store VALUE price;
--   * A CROSS JOIN against a VALUES list of store names + CASE is a one-scan alternative on big
--     tables (UNION ALL scans the table once per column).

SELECT product_id, 'store1' AS store, store1 AS price FROM products_wide WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2', store2 FROM products_wide WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3', store3 FROM products_wide WHERE store3 IS NOT NULL;
