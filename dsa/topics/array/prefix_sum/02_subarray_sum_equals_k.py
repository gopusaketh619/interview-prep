# ============================================================
# PROBLEM: Subarray Sum Equals K
# LeetCode: 560 | https://leetcode.com/problems/subarray-sum-equals-k/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of integers nums and an integer k, return the 
# total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements.
#
# Constraints:
#   - 1 <= len(nums) <= 2 * 10^4
#   - -1000 <= nums[i] <= 1000
#   - -10^7 <= k <= 10^7
#
# Examples:
#   Input:  nums = [1, 1, 1], k = 2
#   Output: 2
#   Explanation: [1,1] at index (0,1) and (1,2)
#
#   Input:  nums = [1, 2, 3], k = 3
#   Output: 2
#   Explanation: [1,2] and [3]
#
#   Input:  nums = [1, -1, 0], k = 0
#   Output: 3
#
# Hint: Use prefix sum + hashmap.
#       If prefix[j] - prefix[i] == k, then subarray (i,j] sums to k.
#       Store counts of prefix sums seen so far in a hashmap.
# ============================================================


def subarray_sum(nums, k):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert subarray_sum([1, 1, 1], 2) == 2
assert subarray_sum([1, 2, 3], 3) == 2
assert subarray_sum([1, -1, 0], 0) == 3
assert subarray_sum([1], 1) == 1
assert subarray_sum([1], 0) == 0
print("All test cases passed!")
