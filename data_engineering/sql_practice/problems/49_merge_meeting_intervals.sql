-- =============================================================================
-- 49. Merge overlapping meetings per room                      Difficulty: Hard
-- Topic: Intervals                            Inspired by: LeetCode 56 "Merge Intervals" in SQL (Google, Uber)
-- Tables: meetings                            Schema: python3 run.py --schema misc
-- =============================================================================
-- For each room, merge overlapping bookings into continuous busy blocks.
--
-- Clarifications:
--   * Bookings that touch (one ends exactly when the next starts) are merged.
--   * A booking can sit entirely inside another, longer booking.
--
-- Output columns: room, start_ts, end_ts
-- Row order: any
-- Check: python3 run.py 49
-- =============================================================================

-- YOUR SQL BELOW

