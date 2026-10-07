-- 22. Warmer than the previous calendar day: reference solution
--
-- Approach: self-join each reading to the reading dated exactly one day earlier.
-- Trap: LAG(temperature) OVER (ORDER BY record_date) compares 2025-01-05 against 2025-01-03
--       (01-04 is missing) and wrongly returns id 4.
-- Alternative: LAG both columns and require LAG(record_date) = record_date - 1.

SELECT w.id
FROM weather w
JOIN weather y
  ON y.record_date = w.record_date - INTERVAL 1 DAY
WHERE w.temperature > y.temperature;
