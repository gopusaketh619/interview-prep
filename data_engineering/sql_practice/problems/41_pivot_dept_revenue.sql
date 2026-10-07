-- =============================================================================
-- 41. Pivot monthly revenue into columns                       Difficulty: Medium
-- Topic: Pivot                                Inspired by: LeetCode 1179 "Reformat Department Table"
-- Tables: dept_revenue                        Schema: python3 run.py --schema misc
-- =============================================================================
-- Reshape dept_revenue (one row per department per month) into one row per department with a
-- revenue column for each of Jan, Feb, Mar, and Apr.
--
-- Clarifications:
--   * A month with no revenue for that department is NULL (not 0).
--
-- Output columns: id, jan_revenue, feb_revenue, mar_revenue, apr_revenue
-- Row order: any
-- Check: python3 run.py 41
-- =============================================================================

-- YOUR SQL BELOW

