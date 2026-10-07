-- 45. Apply a CDC log to get current state: reference solution
--
-- Approach: with full row images, the current state is simply the last change per key by lsn.
--           If that last change is a delete, the key is gone.
-- Traps:
--   * Filtering out 'D' rows BEFORE picking the latest change resurrects deleted customer 11
--     (its last surviving row would be the insert). Pick the latest first, then drop deletes.
--   * Ordering by op_ts or load order instead of lsn. Timestamps can tie or skew; lsn cannot.
-- In production (incremental): MERGE INTO target USING (latest change per key in this batch)
--   WHEN MATCHED AND op = 'D' THEN DELETE
--   WHEN MATCHED THEN UPDATE SET ...
--   WHEN NOT MATCHED AND op <> 'D' THEN INSERT ...

WITH latest AS (
    SELECT customer_id, op, email, tier
    FROM cdc_log
    QUALIFY ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY lsn DESC) = 1
)
SELECT customer_id, email, tier
FROM latest
WHERE op <> 'D';
