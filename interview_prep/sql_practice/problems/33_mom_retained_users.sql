-- =============================================================================
-- 33. Month-over-month retained users                          Difficulty: Hard
-- Topic: Retention                            Inspired by: DataLemur (Facebook) "Active User Retention"
-- Tables: logins                              Schema: python3 run.py --schema events
-- =============================================================================
-- A user is active in a month if they logged in at least once that month. For each month, count
-- the users who were active in that month AND in the previous calendar month.
--
-- Clarifications:
--   * month is a 'YYYY-MM' string.
--   * Only return months with at least one retained user.
--
-- Output columns: month, retained_users
-- Row order: month ascending
-- Check: python3 run.py 33
-- =============================================================================

-- YOUR SQL BELOW

