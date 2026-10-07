-- =============================================================================
-- 30. Average days from first to second order                  Difficulty: Medium
-- Topic: Event analytics                      Inspired by: DataLemur / StrataScratch "time to second purchase"
-- Tables: orders                              Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- Among customers with at least two orders, compute the average number of days between their
-- first and second order.
--
-- Clarifications:
--   * Order a customer's orders by order_date, ties broken by order_id.
--   * Ignore guest orders. Round to 2 decimals.
--
-- Output columns: avg_days_to_second_order
-- Row order: any (single row)
-- Check: python3 run.py 30
-- =============================================================================

-- YOUR SQL BELOW

