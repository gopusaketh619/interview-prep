-- =============================================================================
-- 11. Top 3 distinct salaries per department                   Difficulty: Hard
-- Topic: Ranking windows                      Inspired by: LeetCode 185
-- Tables: departments, employees              Schema: python3 run.py --schema hr
-- =============================================================================
-- A "high earner" is an employee whose salary is in the top 3 DISTINCT salaries of their
-- department. Return every high earner.
--
-- Clarifications:
--   * If two people share a salary, both are returned and that salary counts once toward the 3.
--
-- Output columns: dept_name, employee, salary
-- Row order: any
-- Check: python3 run.py 11
-- =============================================================================

-- YOUR SQL BELOW

