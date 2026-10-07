# ============================================================
# PROBLEM: Two Sum II - Input Array is Sorted
# LeetCode: 167 | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium | Time to Solve: 15 min
# ============================================================
# Given a 1-indexed array of integers that is already sorted 
# in non-decreasing order, find two numbers such that they add 
# up to a specific target number.
#
# Return the indices of the two numbers (1-indexed).
# You may not use the same element twice.
# Exactly one solution is guaranteed.
#
# Constraints:
#   - 2 <= len(numbers) <= 3 * 10^4
#   - -1000 <= numbers[i] <= 1000
#   - numbers is sorted in non-decreasing order
#   - -1000 <= target <= 1000
#
# Examples:
#   Input:  numbers = [2, 7, 11, 15], target = 9
#   Output: [1, 2]
#   Explanation: 2 + 7 = 9, indices are 1 and 2
#
#   Input:  numbers = [2, 3, 4], target = 6
#   Output: [1, 3]
#
#   Input:  numbers = [-1, 0], target = -1
#   Output: [1, 2]
# ============================================================


def two_sum_sorted(numbers, target):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
assert two_sum_sorted([-1, 0], -1) == [1, 2]
assert two_sum_sorted([1, 2, 3, 4, 5], 9) == [4, 5]
print("All test cases passed!")
