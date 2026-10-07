-- =============================================================================
-- 10. Percentage of immediate first orders                     Difficulty: Medium
-- Topic: Aggregation                          Inspired by: LeetCode 1174
-- Tables: orders                              Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- An order is "immediate" if its preferred_delivery_date equals its order_date. Find the
-- percentage of customers whose FIRST order was immediate.
--
-- Clarifications:
--   * A customer's first order is the one with the earliest order_date (ties: lowest order_id).
--   * Ignore guest orders (NULL customer_id).
--   * Round to 2 decimals, e.g. 66.67.
--
-- Output columns: immediate_percentage
-- Row order: any (single row)
-- Check: python3 run.py 10
-- =============================================================================

-- YOUR SQL BELOW

