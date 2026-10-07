-- =============================================================================
-- 44. Latest record per key with tie-breaker                   Difficulty: Medium
-- Topic: Data engineering (deduplication)     Inspired by: every DE screen; Snowflake/dbt "dedupe staging"
-- Tables: customer_updates                    Schema: python3 run.py --schema cdc
-- =============================================================================
-- customer_updates is an append-only feed. Produce exactly one row per customer: the version with
-- the latest updated_at.
--
-- Clarifications:
--   * If two versions share the same updated_at, the one with the later ingested_at wins.
--   * Late-arriving data exists: a row can be ingested later but describe an older update.
--   * The feed can contain exact duplicate rows. Still return one row per customer.
--
-- Output columns: customer_id, email, updated_at
-- Row order: any
-- Check: python3 run.py 44
-- =============================================================================

-- YOUR SQL BELOW

