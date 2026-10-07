-- 50. Users with overlapping subscriptions: reference solution
--
-- Approach: two intervals [a.start, a.end] and [b.start, b.end] overlap exactly when
--           a.start <= b.end AND b.start <= a.end. Memorize this; every other formulation is a
--           pile of cases. Replace a NULL end with a far-future date first.
-- Traps:
--   * NULL end_date makes the comparison UNKNOWN, so user 3's open-ended plan never "overlaps".
--   * `a.sub_id <> b.sub_id` is required, or every subscription overlaps itself.
--   * Strict `<` would miss user 4, whose subscriptions share exactly 2025-04-30.
-- Faster alternative for many subscriptions per user: sort by start and compare each start to
--   the running MAX(end) of earlier rows (problem 49's pattern), avoiding the self-join.

WITH subs AS (
    SELECT sub_id, user_id, start_date, COALESCE(end_date, DATE '9999-12-31') AS end_date
    FROM subscriptions
)
SELECT u.user_id,
       EXISTS (
           SELECT 1
           FROM subs a
           JOIN subs b
             ON a.user_id = b.user_id
            AND a.sub_id < b.sub_id
            AND a.start_date <= b.end_date
            AND b.start_date <= a.end_date
           WHERE a.user_id = u.user_id
       ) AS has_overlap
FROM (SELECT DISTINCT user_id FROM subs) u;
