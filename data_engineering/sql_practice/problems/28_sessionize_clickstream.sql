-- =============================================================================
-- 28. Sessionize a clickstream                                 Difficulty: Hard
-- Topic: Event analytics (sessionization)     Inspired by: Google / Meta / Amplitude-style sessionization
-- Tables: events                              Schema: python3 run.py --schema events
-- =============================================================================
-- Split each user's events into sessions. A new session starts when more than 30 minutes have
-- passed since that user's previous event. Number each user's sessions 1, 2, 3, ... in time order.
--
-- Clarifications:
--   * A gap of exactly 30 minutes stays in the same session.
--   * Sessions do not span users.
--
-- Output columns: user_id, session_id, session_start, session_end, event_count
-- Row order: any
-- Check: python3 run.py 28
-- =============================================================================

-- YOUR SQL BELOW

