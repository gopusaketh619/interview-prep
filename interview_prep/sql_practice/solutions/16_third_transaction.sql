-- 16. Each user's third transaction: reference solution
--
-- Approach: ROW_NUMBER with a fully deterministic ORDER BY (date, then id).
-- Traps:
--   * RANK or DENSE_RANK on trans_date alone gives user 3's two 2025-01-20 transactions the same
--     rank, so "rank = 3" returns the wrong row or nothing.
--   * ROW_NUMBER without the trans_id tie-breaker is non-deterministic: it can pass today and
--     fail on a re-run. Always make window ORDER BYs unique when you need exactly one row.

SELECT user_id, trans_id, amount, trans_date
FROM transactions
QUALIFY ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY trans_date, trans_id) = 3;
