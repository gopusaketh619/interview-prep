-- =============================================================================
-- 14. Top-quartile customers by spend                          Difficulty: Medium
-- Topic: Ranking windows (NTILE)              Inspired by: Amazon / Stripe "top N% of customers"
-- Tables: orders, order_items                 Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- Compute each customer's lifetime spend and split customers into 4 buckets with NTILE(4),
-- ordered by spend from highest to lowest. Return the customers in the top bucket.
--
-- Clarifications:
--   * spend = SUM(quantity * unit_price). Ignore guest orders.
--   * Only customers with at least one order are bucketed.
--   * Order the NTILE by total_spend DESC, then customer_id, so the bucketing is deterministic.
--
-- Output columns: customer_id, total_spend
-- Row order: any
-- Check: python3 run.py 14
-- =============================================================================

-- YOUR SQL BELOW

