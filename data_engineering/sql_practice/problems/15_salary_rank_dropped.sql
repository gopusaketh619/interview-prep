-- =============================================================================
-- 15. Employees whose salary rank dropped                      Difficulty: Hard
-- Topic: Ranking windows                      Inspired by: common "rank change between periods" question
-- Tables: salary_history, employees, departments     Schema: python3 run.py --schema hr
-- =============================================================================
-- Within each department, rank employees by salary for 2024 and separately for 2025 using
-- DENSE_RANK (1 = highest paid). Return employees whose rank got worse (a larger number) in 2025.
--
-- Clarifications:
--   * An employee's department comes from `employees`.
--   * Only employees who have a salary_history row in BOTH years can be compared.
--   * Each year is ranked only among employees who have a row for that year.
--
-- Output columns: dept_name, employee, rank_2024, rank_2025
-- Row order: any
-- Check: python3 run.py 15
-- =============================================================================

-- YOUR SQL BELOW

