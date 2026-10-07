-- =============================================================================
-- 43. Distinct products sold per date                          Difficulty: Medium
-- Topic: String aggregation                   Inspired by: LeetCode 1484 "Group Sold Products By The Date"
-- Tables: sales_log                           Schema: python3 run.py --schema misc
-- =============================================================================
-- For each sell_date, return the number of distinct products sold and their names as a single
-- comma-separated string sorted alphabetically.
--
-- Clarifications:
--   * The same product can be sold more than once on a date; list it once.
--   * No spaces after commas, e.g. 'Basketball,Headphone,T-Shirt'.
--
-- Output columns: sell_date, num_sold, products
-- Row order: sell_date ascending
-- Check: python3 run.py 43
-- =============================================================================

-- YOUR SQL BELOW

