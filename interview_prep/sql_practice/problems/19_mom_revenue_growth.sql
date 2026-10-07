-- =============================================================================
-- 19. Month-over-month revenue growth                          Difficulty: Medium
-- Topic: LAG / LEAD                           Inspired by: StrataScratch (Amazon) "Monthly Percentage Difference"
-- Tables: orders, order_items                 Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- Report total revenue per month and the percentage change from the previous month.
--
-- Clarifications:
--   * revenue = SUM(quantity * unit_price) over all orders, including guest orders.
--   * month is a 'YYYY-MM' string.
--   * growth_pct = 100 * (revenue - prev_month_revenue) / prev_month_revenue, rounded to 2.
--   * For the first month, prev_month_revenue and growth_pct are NULL.
--
-- Output columns: month, revenue, prev_month_revenue, growth_pct
-- Row order: month ascending
-- Check: python3 run.py 19
-- =============================================================================

-- YOUR SQL BELOW

