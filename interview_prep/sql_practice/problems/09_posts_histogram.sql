-- =============================================================================
-- 09. Histogram of posts per user                              Difficulty: Medium
-- Topic: Aggregation                          Inspired by: DataLemur (Twitter) "Histogram of Tweets"
-- Tables: posts                               Schema: python3 run.py --schema social
-- =============================================================================
-- For posts created in calendar year 2025, build a histogram: for each number of posts a user
-- made, how many users made exactly that many.
--
-- Clarifications:
--   * Only count posts created in 2025 (created_at is a TIMESTAMP).
--   * Users with no 2025 posts do not appear.
--
-- Output columns: post_bucket, users_num
-- Row order: post_bucket ascending
-- Check: python3 run.py 9
-- =============================================================================

-- YOUR SQL BELOW

