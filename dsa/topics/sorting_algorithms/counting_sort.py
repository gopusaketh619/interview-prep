# ============================================================
# PROBLEM: Counting Sort
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Implement the Counting Sort algorithm. Counting Sort is a
# non-comparison-based sorting algorithm that works well when
# the range of input values is small.
#
# Constraints:
#   - 1 <= len(arr) <= 10^5
#   - 0 <= arr[i] <= k (small range of non-negative integers)
#
# Examples:
#   Input:  arr = [4, 2, 2, 8, 3, 3, 1]
#   Output: [1, 2, 2, 3, 3, 4, 8]
# ============================================================

def counting_sort(arr):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
assert counting_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert counting_sort([]) == []
assert counting_sort([0, 0, 0]) == [0, 0, 0]
print("All test cases passed!")
