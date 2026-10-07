-- 41. Pivot monthly revenue into columns: reference solution
--
-- Approach: conditional aggregation, the portable pivot. Works in every engine and is what
--           interviewers expect you to write by hand.
-- Notes:
--   * SUM(CASE WHEN month = 'Jan' THEN revenue END) is the pre-FILTER spelling. Leaving out ELSE 0
--     is what keeps empty months NULL.
--   * DuckDB and Snowflake also have PIVOT:
--       PIVOT dept_revenue ON month IN ('Jan', 'Feb', 'Mar', 'Apr') USING SUM(revenue) GROUP BY id;
--     but you must list the values; dynamic pivots need generated SQL.

SELECT id,
       SUM(revenue) FILTER (WHERE month = 'Jan') AS jan_revenue,
       SUM(revenue) FILTER (WHERE month = 'Feb') AS feb_revenue,
       SUM(revenue) FILTER (WHERE month = 'Mar') AS mar_revenue,
       SUM(revenue) FILTER (WHERE month = 'Apr') AS apr_revenue
FROM dept_revenue
GROUP BY id;
