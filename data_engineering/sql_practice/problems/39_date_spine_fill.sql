-- =============================================================================
-- 39. Daily signups with a date spine                          Difficulty: Medium
-- Topic: Recursive CTEs (generate a calendar) Inspired by: common dashboard "fill missing days" question
-- Tables: users                               Schema: python3 run.py --schema events
-- =============================================================================
-- Report the number of signups for every day from 2025-01-01 through 2025-01-10 inclusive,
-- including days with zero signups.
--
-- Clarifications:
--   * Generate the calendar with a recursive CTE (no calendar table exists). generate_series is a
--     fine follow-up, but practice the recursive version: not every engine has generate_series.
--
-- Output columns: signup_date, signups
-- Row order: signup_date ascending
-- Check: python3 run.py 39
-- =============================================================================

-- YOUR SQL BELOW

