-- =============================================================================
-- 20. Year-over-year spend growth per product                  Difficulty: Medium
-- Topic: LAG / self-join on period            Inspired by: DataLemur (Wayfair) "Y-on-Y Growth Rate"
-- Tables: product_spend                       Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- For each product and each year it had spend, return that year's total spend, the previous
-- calendar year's total spend, and the year-over-year growth rate as a percentage.
--
-- Clarifications:
--   * "Previous year" means calendar year - 1. If the product had no spend that year,
--     prev_year_spend and yoy_rate are NULL.
--   * yoy_rate = 100 * (curr - prev) / prev, rounded to 2 decimals.
--
-- Output columns: year, product_id, curr_year_spend, prev_year_spend, yoy_rate
-- Row order: any
-- Check: python3 run.py 20
-- =============================================================================

-- YOUR SQL BELOW

