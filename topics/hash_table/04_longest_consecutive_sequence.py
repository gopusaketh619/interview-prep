# ============================================================
# PROBLEM: Longest Consecutive Sequence
# LeetCode: 128 | https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an unsorted array of integers nums, return the length
# of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
#
# Constraints:
#   - 0 <= len(nums) <= 10^5
#   - -10^9 <= nums[i] <= 10^9
#
# Examples:
#   Input:  nums = [100, 4, 200, 1, 3, 2]
#   Output: 4
#   Explanation: [1, 2, 3, 4] is the longest consecutive sequence
#
#   Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#   Output: 9
# ============================================================

def longest_consecutive(nums):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert longest_consecutive([]) == 0
assert longest_consecutive([1]) == 1
assert longest_consecutive([1, 2, 0, 1]) == 3
print("All test cases passed!")
