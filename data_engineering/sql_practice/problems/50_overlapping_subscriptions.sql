-- =============================================================================
-- 50. Users with overlapping subscriptions                     Difficulty: Hard
-- Topic: Intervals                            Inspired by: StrataScratch / DataLemur "overlapping subscriptions"
-- Tables: subscriptions                       Schema: python3 run.py --schema subscriptions
-- =============================================================================
-- For every user, report whether any two of their own subscriptions overlap in time.
--
-- Clarifications:
--   * start_date and end_date are both inclusive. Sharing a single day counts as overlap.
--   * A NULL end_date means the subscription is still active (open-ended).
--   * A subscription that ends on Jan 31 and a renewal that starts Feb 1 do not overlap.
--   * Return every user who has any subscription, with TRUE or FALSE.
--
-- Output columns: user_id, has_overlap
-- Row order: any
-- Check: python3 run.py 50
-- =============================================================================

-- YOUR SQL BELOW

