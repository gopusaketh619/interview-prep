# ============================================================
# INTERVAL - PATTERN TEMPLATE
# ============================================================
#
# Interval problems deal with ranges [start, end].
# Usually require sorting by start time first.
#
# KEY TECHNIQUES:
#
#   1. Merge Overlapping Intervals:
#      intervals.sort(key=lambda x: x[0])
#      merged = [intervals[0]]
#      for start, end in intervals[1:]:
#          if start <= merged[-1][1]:   # overlaps
#              merged[-1][1] = max(merged[-1][1], end)
#          else:
#              merged.append([start, end])
#
#   2. Insert Interval:
#      Find position, merge with overlapping, keep non-overlapping.
#
#   3. Overlap Check:
#      Two intervals [a, b] and [c, d] overlap if: a <= d and c <= b
#      No overlap if: b < c or d < a
#
#   4. Sweep Line:
#      Convert intervals to events (+1 at start, -1 at end).
#      Sort events, sweep to find max overlap / conflicts.
#
# WHEN TO USE:
#   - "Merge overlapping..."
#   - "Find conflicts / maximum overlap"
#   - "Insert into sorted intervals"
#   - Meeting rooms, scheduling
#   - Interval intersection / union
#
# TIME: O(n log n) for sorting, O(n) for sweep
# SPACE: O(n) for output
# ============================================================
