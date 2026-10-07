-- =============================================================================
-- 16. Each user's third transaction                            Difficulty: Medium
-- Topic: Ranking windows                      Inspired by: DataLemur (Uber) "User's Third Transaction"
-- Tables: transactions                        Schema: python3 run.py --schema ecommerce
-- =============================================================================
-- Return the third transaction of every user, ordering each user's transactions by trans_date.
--
-- Clarifications:
--   * Several transactions can share a trans_date; break ties by trans_id (lower first).
--   * Users with fewer than 3 transactions are not returned.
--
-- Output columns: user_id, trans_id, amount, trans_date
-- Row order: any
-- Check: python3 run.py 16
-- =============================================================================

-- YOUR SQL BELOW

