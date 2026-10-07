-- 27. Compress daily run states into periods: reference solution
--
-- Approach: within each state, run_date - ROW_NUMBER() is constant across consecutive calendar days.
--           Group by (state, key).
-- Trap: the common "ROW_NUMBER overall minus ROW_NUMBER per state" version only looks at row order,
--       so it merges 01-05 and 01-07 into one 'succeeded' period even though 01-06 had no run.
--       Subtracting from the DATE makes calendar gaps break the island.

WITH keyed AS (
    SELECT run_date, state,
           run_date - CAST(ROW_NUMBER() OVER (PARTITION BY state ORDER BY run_date) AS INTEGER)
               AS period_key
    FROM task_runs
)
SELECT state AS period_state,
       MIN(run_date) AS start_date,
       MAX(run_date) AS end_date
FROM keyed
GROUP BY state, period_key
ORDER BY start_date;
