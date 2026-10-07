-- 05. Friend recommendations by mutual friends: reference solution
--
-- Approach: make the edge list symmetric with UNION ALL, then join two edges that share the same
--           friend (a.friend = b.friend). Each match is one mutual friend of a.user and b.user.
--           Exclude existing friendships with NOT EXISTS and keep pairs with >= 2 matches.
-- Traps:
--   * Querying `friendships` directly only follows edges in one direction and misses most pairs.
--   * Forgetting `a.u <> b.u` pairs every user with themselves.
--   * Forgetting the existing-friend filter recommends people who are already friends (e.g. 1 and 2).

WITH f AS (
    SELECT user_a AS u, user_b AS v FROM friendships
    UNION ALL
    SELECT user_b AS u, user_a AS v FROM friendships
)
SELECT a.u AS user_id,
       b.u AS recommended_id,
       COUNT(*) AS mutual_friends
FROM f a
JOIN f b
  ON a.v = b.v
 AND a.u <> b.u
WHERE NOT EXISTS (
    SELECT 1 FROM f x WHERE x.u = a.u AND x.v = b.u
)
GROUP BY a.u, b.u
HAVING COUNT(*) >= 2;
