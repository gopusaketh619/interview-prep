-- 24. Longest login streak per user: reference solution
--
-- Approach: dedupe to one row per (user, day). Then day - ROW_NUMBER() is the same date for every
--           day in an unbroken streak (each day goes up by 1 and so does the row number).
-- Traps:
--   * Without DISTINCT days, user 1's two logins on 01-02 shift the row numbers and break the streak.
--     DENSE_RANK on the date also works and avoids the separate DISTINCT.
--   * Comparing timestamps instead of dates: 01-31 23:00 -> 02-01 01:00 is a 2-hour gap but still
--     consecutive days (user 4).

WITH login_days AS (
    SELECT DISTINCT user_id, CAST(login_ts AS DATE) AS login_day
    FROM logins
),
streaks AS (
    SELECT user_id,
           login_day - CAST(ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_day) AS INTEGER)
               AS streak_key
    FROM login_days
),
lengths AS (
    SELECT user_id, streak_key, COUNT(*) AS streak_len
    FROM streaks
    GROUP BY user_id, streak_key
)
SELECT user_id, MAX(streak_len) AS longest_streak
FROM lengths
GROUP BY user_id;
