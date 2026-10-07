-- =============================================================================
-- 37. Repeat-purchase rate within 30 days                      Difficulty: Medium
-- Topic: Retention                            Inspired by: Amazon / Instacart "repeat purchase" metrics
-- Tables: orders                              Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- A customer is a "fast repeater" if any two of their consecutive orders are at most 30 days
-- apart. Return the percentage of ordering customers who are fast repeaters.
--
-- Clarifications:
--   * The denominator is every customer with at least one order (ignore guest orders).
--   * Order each customer's orders by order_date, ties broken by order_id. Round to 2 decimals.
--
-- Output columns: repeat_rate_pct
-- Row order: any (single row)
-- Check: python3 run.py 37
-- =============================================================================

-- YOUR SQL BELOW

