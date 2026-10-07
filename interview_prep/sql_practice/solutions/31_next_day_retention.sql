-- 31. Fraction of players back the day after first login: reference solution
--
-- Approach: find each player's first date, LEFT JOIN activity on exactly first_date + 1 day,
--           and divide matched players by all players.
-- Traps:
--   * Checking "any second login" rather than "the next calendar day" (player 4 returns two days
--     later; player 3 returns months later).
--   * Day + 1 across a month boundary (player 5: 02-28 -> 03-01). Use date arithmetic, never
--     DAY(event_date) + 1.
--   * Integer division returns 0 in Postgres/SQL Server; use 1.0 * or AVG.

WITH first_login AS (
    SELECT player_id, MIN(event_date) AS first_date
    FROM activity
    GROUP BY player_id
)
SELECT ROUND(COUNT(DISTINCT a.player_id) * 1.0 / COUNT(DISTINCT f.player_id), 2) AS fraction
FROM first_login f
LEFT JOIN activity a
       ON a.player_id = f.player_id
      AND a.event_date = f.first_date + INTERVAL 1 DAY;
