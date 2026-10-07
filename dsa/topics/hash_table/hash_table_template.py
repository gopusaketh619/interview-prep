# ============================================================
# HASH TABLE - PATTERN TEMPLATE
# ============================================================
#
# Hash tables (dict/set in Python) provide O(1) average-case
# lookup, insertion, and deletion by mapping keys to values
# through a hash function.
#
# COMMON PATTERNS:
#
#   1. Two-Sum Pattern (complement lookup):
#      seen = {}
#      for i, num in enumerate(arr):
#          complement = target - num
#          if complement in seen:
#              return [seen[complement], i]
#          seen[num] = i
#
#   2. Frequency Counting:
#      from collections import Counter
#      freq = Counter(arr)
#      # or manually:
#      freq = {}
#      for x in arr:
#          freq[x] = freq.get(x, 0) + 1
#
#   3. Grouping by Key:
#      from collections import defaultdict
#      groups = defaultdict(list)
#      for item in items:
#          groups[key_fn(item)].append(item)
#
#   4. Set for Existence Checks:
#      seen = set()
#      for x in arr:
#          if x in seen: ...
#          seen.add(x)
#
# WHEN TO USE:
#   - Need O(1) lookup by key
#   - Counting frequencies
#   - Finding pairs/complements
#   - Deduplication
#   - Grouping elements
#   - Caching/memoization
#
# TIME: O(1) average for get/set/delete
# SPACE: O(n) for n elements stored
# ============================================================
