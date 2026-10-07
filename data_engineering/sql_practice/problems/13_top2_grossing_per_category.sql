-- =============================================================================
-- 13. Top 2 grossing products per category                     Difficulty: Medium
-- Topic: Ranking windows                      Inspired by: DataLemur (Amazon) "Highest-Grossing Items"
-- Tables: orders, order_items, products       Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- For Q1 2025 (January through March), return the two highest-grossing products in each category.
--
-- Clarifications:
--   * revenue = SUM(quantity * unit_price), using the price actually charged on the order line.
--   * Use order_date to decide whether an order is in Q1. Include guest orders.
--
-- Output columns: category, product, revenue
-- Row order: any
-- Check: python3 run.py 13
-- =============================================================================

-- YOUR SQL BELOW

