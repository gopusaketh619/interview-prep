-- 09. Histogram of posts per user: reference solution
--
-- Approach: aggregate twice. First posts per user, then users per post count.
-- Traps:
--   * `created_at BETWEEN '2025-01-01' AND '2025-12-31'` drops anything after midnight on Dec 31,
--     because the upper bound is cast to 2025-12-31 00:00:00. Use a half-open range [start, next start).
--   * Post 1 is at 2024-12-31 23:59 and must be excluded; post 2 at 2025-01-01 00:00 is included.
--   * Wrapping the column in a function (YEAR(created_at) = 2025) is correct but prevents partition
--     pruning / index use on big tables. The half-open range is the habit to show.

WITH per_user AS (
    SELECT user_id, COUNT(*) AS post_count
    FROM posts
    WHERE created_at >= TIMESTAMP '2025-01-01'
      AND created_at <  TIMESTAMP '2026-01-01'
    GROUP BY user_id
)
SELECT post_count AS post_bucket,
       COUNT(*)   AS users_num
FROM per_user
GROUP BY post_count
ORDER BY post_bucket;
