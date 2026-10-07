-- =============================================================================
-- 12. Top-selling product per category per month               Difficulty: Medium
-- Topic: Ranking windows                      Inspired by: Amazon / StrataScratch "best-selling item per month"
-- Tables: orders, order_items, products       Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- For every month and product category, return the product(s) with the highest total quantity
-- sold that month.
--
-- Clarifications:
--   * month is a 'YYYY-MM' string based on order_date.
--   * Include guest orders; every order counts.
--   * If products tie for the top quantity, return all of them.
--
-- Output columns: month, category, product, total_quantity
-- Row order: any
-- Check: python3 run.py 12
-- =============================================================================

-- YOUR SQL BELOW

