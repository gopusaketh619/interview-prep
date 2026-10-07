-- =============================================================================
-- 03. Products frequently bought together                      Difficulty: Hard
-- Topic: Joins and set logic                  Inspired by: DataLemur (Walmart) "Frequently Purchased Pairs"
-- Tables: order_items, products               Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- Find every pair of different products that appear together in at least 2 distinct orders.
--
-- Clarifications:
--   * Report each pair once, with the lower product_id as product_a.
--   * A product can appear on more than one line of the same order; that order still counts once.
--
-- Output columns: product_a (name), product_b (name), orders_together
-- Row order: orders_together DESC, then product_a's id, then product_b's id
-- Check: python3 run.py 3
-- =============================================================================

-- YOUR SQL BELOW

