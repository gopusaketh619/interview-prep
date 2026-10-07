-- 44. Latest record per key with tie-breaker: reference solution
--
-- Approach: ROW_NUMBER over the business key, ordered by event time then ingest time, keep 1.
-- Traps:
--   * Ordering by ingested_at alone picks customer 2's late-arriving older email (b0).
--   * RANK keeps both of customer 3's identical rows; ROW_NUMBER always returns exactly one.
--   * MAX(updated_at) + join back returns two rows for customer 1 (a2 and a3 share updated_at).
-- In production: this is the body of a dbt incremental model or a MERGE source; add a final
--   tie-breaker (e.g. a file offset or hash) so re-runs are deterministic.

SELECT customer_id, email, updated_at
FROM customer_updates
QUALIFY ROW_NUMBER() OVER (
    PARTITION BY customer_id
    ORDER BY updated_at DESC, ingested_at DESC
) = 1;
