-- =============================================================================
-- 42. Unpivot store prices                                     Difficulty: Medium
-- Topic: Unpivot                              Inspired by: LeetCode 1795 "Rearrange Products Table"
-- Tables: products_wide                       Schema: python3 run.py --schema misc
-- =============================================================================
-- products_wide has one price column per store. Reshape it to one row per (product, store) where
-- the product is sold.
--
-- Clarifications:
--   * A NULL price means the product is not sold at that store; leave that row out.
--   * store is the column name as a string: 'store1', 'store2', or 'store3'.
--
-- Output columns: product_id, store, price
-- Row order: any
-- Check: python3 run.py 42
-- =============================================================================

-- YOUR SQL BELOW

