-- =============================================================================
-- 25. 3+ consecutive high-traffic rows                         Difficulty: Hard
-- Topic: Gaps and islands                     Inspired by: LeetCode 601 "Human Traffic of Stadium"
-- Tables: stadium                             Schema: python3 run.py --schema misc
-- =============================================================================
-- Return every row that belongs to a run of 3 or more rows with consecutive ids where
-- people >= 100.
--
-- Clarifications:
--   * "Consecutive" is by id (ids 5, 6, 7, 8 are consecutive even if a visit_date is skipped).
--   * Return all rows of each qualifying run, not just the first 3.
--
-- Output columns: id, visit_date, people
-- Row order: visit_date ascending
-- Check: python3 run.py 25
-- =============================================================================

-- YOUR SQL BELOW

