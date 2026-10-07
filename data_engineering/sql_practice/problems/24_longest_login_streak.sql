-- =============================================================================
-- 24. Longest login streak per user                            Difficulty: Hard
-- Topic: Gaps and islands                     Inspired by: common Meta / Amazon "consecutive days" question
-- Tables: logins                              Schema: python3 run.py --schema events
-- =============================================================================
-- For every user who has logged in at least once, return the length of their longest streak of
-- consecutive calendar days with at least one login.
--
-- Clarifications:
--   * login_ts is a TIMESTAMP; a user can log in several times on the same day.
--   * Streaks can cross month boundaries.
--
-- Output columns: user_id, longest_streak
-- Row order: any
-- Check: python3 run.py 24
-- =============================================================================

-- YOUR SQL BELOW

