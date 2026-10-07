# ============================================================
# PROBLEM: Minimum Size Subarray Sum
# LeetCode: 209 | https://leetcode.com/problems/minimum-size-subarray-sum/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of positive integers nums and a positive 
# integer target, return the minimal length of a subarray whose 
# sum is greater than or equal to target. If no such subarray 
# exists, return 0.
#
# Constraints:
#   - 1 <= target <= 10^9
#   - 1 <= len(nums) <= 10^5
#   - 1 <= nums[i] <= 10^4
#
# Examples:
#   Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
#   Output: 2
#   Explanation: Subarray [4, 3] has minimal length
#
#   Input:  target = 4, nums = [1, 4, 4]
#   Output: 1
#
#   Input:  target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
#   Output: 0
#
# Note: This can be solved with sliding window (O(n)) OR
#       binary search on prefix sums (O(n log n)).
#       Try both approaches!
# ============================================================


def min_subarray_len(target, nums):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
assert min_subarray_len(4, [1, 4, 4]) == 1
assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert min_subarray_len(15, [1, 2, 3, 4, 5]) == 5
assert min_subarray_len(5, [2, 3, 1, 1, 1, 1, 1]) == 2
print("All test cases passed!")
