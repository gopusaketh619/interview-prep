-- =============================================================================
-- 05. Friend recommendations by mutual friends                 Difficulty: Hard
-- Topic: Joins and set logic                  Inspired by: Meta "People You May Know"
-- Tables: friendships                         Schema: python3 run.py --schema social
-- =============================================================================
-- Recommend user Y to user X when X and Y are not already friends and they share at least
-- 2 mutual friends.
--
-- Clarifications:
--   * Friendship is undirected but stored once per pair, always with user_a < user_b.
--   * Return both directions: if 1 is recommended to 4, 4 is also recommended to 1.
--   * Never recommend a user to themselves.
--
-- Output columns: user_id, recommended_id, mutual_friends
-- Row order: any
-- Check: python3 run.py 5
-- =============================================================================

-- YOUR SQL BELOW

