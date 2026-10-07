# ============================================================
# BINARY SEARCH - PATTERN TEMPLATE
# ============================================================
#
# Binary search reduces the search space by half each step.
# Works on SORTED arrays or any monotonic condition.
#
# TEMPLATE 1 - Find exact target:
#
#   left, right = 0, len(arr) - 1
#   while left <= right:
#       mid = (left + right) // 2
#       if arr[mid] == target:
#           return mid
#       elif arr[mid] < target:
#           left = mid + 1
#       else:
#           right = mid - 1
#   return -1
#
# TEMPLATE 2 - Find boundary (first/last occurrence):
#
#   left, right = 0, len(arr) - 1
#   result = -1
#   while left <= right:
#       mid = (left + right) // 2
#       if condition(mid):
#           result = mid
#           right = mid - 1   # find FIRST (leftmost)
#           # left = mid + 1  # find LAST (rightmost)
#       else:
#           left = mid + 1
#   return result
#
# WHEN TO USE:
#   - Array is sorted
#   - "Find minimum/maximum that satisfies condition"
#   - O(log n) is expected
#   - Search space can be halved by a condition
#
# TIME: O(log n)
# SPACE: O(1)
# ============================================================
