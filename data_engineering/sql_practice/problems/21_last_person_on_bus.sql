-- =============================================================================
-- 21. Last person to fit on the bus                            Difficulty: Medium
-- Topic: Running sum cutoff                   Inspired by: LeetCode 1204
-- Tables: queue                               Schema: python3 run.py --schema misc
-- =============================================================================
-- People board a bus in `turn` order. The bus holds at most 1000 kg. Return the name of the
-- last person who can board without the total weight exceeding the limit.
--
-- Clarifications:
--   * Boarding stops at the first person who would push the total over 1000; nobody after them
--     boards, even if they are light enough.
--   * person_id is not the boarding order; turn is.
--
-- Output columns: person_name
-- Row order: any (single row)
-- Check: python3 run.py 21
-- =============================================================================

-- YOUR SQL BELOW

