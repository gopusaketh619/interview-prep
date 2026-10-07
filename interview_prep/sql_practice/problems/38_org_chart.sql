-- =============================================================================
-- 38. Org chart with depth and path                            Difficulty: Hard
-- Topic: Recursive CTEs (hierarchies)         Inspired by: LeetCode 1270 / Amazon "all reports of a manager"
-- Tables: employees                           Schema: python3 run.py --schema hr
-- =============================================================================
-- Starting from the CEO (the employee with no manager), list every employee with their depth in
-- the org chart and their reporting path from the CEO.
--
-- Clarifications:
--   * The CEO has depth 0 and path 'Alice'.
--   * path joins names with ' > ', e.g. 'Alice > Bob > Carol'.
--
-- Output columns: employee, depth, path
-- Row order: path ascending
-- Check: python3 run.py 38
-- =============================================================================

-- YOUR SQL BELOW

