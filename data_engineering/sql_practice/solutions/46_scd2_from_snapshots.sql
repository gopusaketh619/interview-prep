-- 46. Build SCD Type 2 from daily snapshots: reference solution
--
-- Approach: keep only the snapshots where the tier differs from the previous day's (change points),
--           then each version ends where the next change point begins (LEAD).
-- Traps:
--   * GROUP BY customer_id, tier with MIN/MAX dates merges customer 1's two separate bronze periods
--     into one row spanning the silver period. This is gaps and islands in disguise.
--   * valid_to as the last snapshot date (inclusive) vs the next valid_from (exclusive): pick one
--     convention and say it out loud. Half-open ranges make point-in-time joins simple:
--     valid_from <= d AND (d < valid_to OR valid_to IS NULL).
--   * Hard deletes (a customer missing from later snapshots) are not handled here; you would close
--     the open version at the first snapshot where the key is missing.

WITH changes AS (
    SELECT customer_id, tier, snapshot_date,
           LAG(tier) OVER (PARTITION BY customer_id ORDER BY snapshot_date) AS prev_tier
    FROM customer_snapshots
),
versions AS (
    SELECT customer_id, tier, snapshot_date AS valid_from,
           LEAD(snapshot_date) OVER (PARTITION BY customer_id ORDER BY snapshot_date) AS valid_to
    FROM changes
    WHERE prev_tier IS NULL OR prev_tier <> tier
)
SELECT customer_id, tier, valid_from, valid_to, valid_to IS NULL AS is_current
FROM versions;
