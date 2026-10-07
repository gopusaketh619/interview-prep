# ============================================================
# TWO POINTERS - PATTERN TEMPLATE
# ============================================================
#
# Two pointers is a technique where two indices traverse the
# array (or string) simultaneously to solve problems in O(n).
#
# TYPES:
#   1. Opposite direction: left=0, right=n-1, move toward center
#      - Used for: sorted array pair sum, palindromes, container problems
#
#   2. Same direction: slow and fast pointer
#      - Used for: remove duplicates, partition, linked list cycle
#
#   3. Two arrays: one pointer per array
#      - Used for: merge sorted arrays, intersection
#
# WHEN TO USE:
#   - Array is sorted (or can be sorted)
#   - Looking for pairs/triplets that satisfy a condition
#   - Need to compare elements from both ends
#   - Partitioning or rearranging in-place
#
# TEMPLATE (Opposite Direction):
#
#   left, right = 0, len(arr) - 1
#   while left < right:
#       if condition_met(left, right):
#           record answer
#           left += 1  (or right -= 1)
#       elif need_bigger:
#           left += 1
#       else:
#           right -= 1
#
# TEMPLATE (Same Direction):
#
#   slow = 0
#   for fast in range(len(arr)):
#       if condition:
#           arr[slow] = arr[fast]
#           slow += 1
#   return slow
#
# TIME: O(n) — each pointer moves at most n steps
# SPACE: O(1) — in-place
# ============================================================
