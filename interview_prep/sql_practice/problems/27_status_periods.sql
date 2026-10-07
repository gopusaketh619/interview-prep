-- =============================================================================
-- 27. Compress daily run states into periods                   Difficulty: Hard
-- Topic: Gaps and islands                     Inspired by: LeetCode 1225 "Report Contiguous Dates"
-- Tables: task_runs                           Schema: python3 run.py --schema misc
-- =============================================================================
-- A pipeline runs at most once per day and either 'succeeded' or 'failed'. Compress the history
-- into periods: maximal runs of consecutive calendar days with the same state.
--
-- Clarifications:
--   * A day with no run breaks a period, even if the state is the same on both sides.
--
-- Output columns: period_state, start_date, end_date
-- Row order: start_date ascending
-- Check: python3 run.py 27
-- =============================================================================

-- YOUR SQL BELOW

