# ============================================================
# PROBLEM: Top K Frequent Elements
# LeetCode: 347 | https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an integer array nums and an integer k, return the k
# most frequent elements. You may return the answer in any order.
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - -10^4 <= nums[i] <= 10^4
#   - k is in the range [1, number of unique elements]
#   - Answer is guaranteed to be unique
#
# Examples:
#   Input:  nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
#
#   Input:  nums = [1], k = 1
#   Output: [1]
# ============================================================

def top_k_frequent(nums, k):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert sorted(top_k_frequent([1,1,1,2,2,3], 2)) == [1,2]
assert top_k_frequent([1], 1) == [1]
print("All test cases passed!")
