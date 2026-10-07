# ============================================================
# PROBLEM: Quick Sort
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Implement the Quick Sort algorithm. Quick Sort is a
# divide-and-conquer algorithm that picks a pivot element
# and partitions the array around it.
#
# Constraints:
#   - 1 <= len(arr) <= 10^5
#   - Array can contain duplicates
#
# Examples:
#   Input:  arr = [3, 6, 8, 10, 1, 2, 1]
#   Output: [1, 1, 2, 3, 6, 8, 10]
# ============================================================

def quick_sort(arr):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert quick_sort([1]) == [1]
assert quick_sort([]) == []
assert quick_sort([2, 2, 2]) == [2, 2, 2]
print("All test cases passed!")
