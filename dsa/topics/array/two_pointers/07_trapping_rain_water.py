# ============================================================
# PROBLEM: Trapping Rain Water (Hard)
# LeetCode: 42 | https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard | Time to Solve: 30 min
# ============================================================
# Given n non-negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water it 
# can trap after raining.
#
# Constraints:
#   - n == len(height)
#   - 1 <= n <= 2 * 10^4
#   - 0 <= height[i] <= 10^5
#
# Examples:
#   Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   Output: 6
#
#   Input:  height = [4,2,0,3,2,5]
#   Output: 9
#
#   Input:  height = [1,0,1]
#   Output: 1
#
# Hint: Water at each index = min(max_left, max_right) - height[i]
#       Two pointers can compute this in O(n) time, O(1) space.
# ============================================================


def trap(height):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap([4, 2, 0, 3, 2, 5]) == 9
assert trap([1, 0, 1]) == 1
assert trap([3, 0, 0, 2, 0, 4]) == 10
assert trap([]) == 0
print("All test cases passed!")
