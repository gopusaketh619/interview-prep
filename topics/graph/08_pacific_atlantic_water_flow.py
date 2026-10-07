# ============================================================
# PROBLEM: Pacific Atlantic Water Flow
# LeetCode: 417 | https://leetcode.com/problems/pacific-atlantic-water-flow/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given an m x n matrix of heights, water can flow to adjacent
# cells (up/down/left/right) if the adjacent cell's height is
# less than or equal. Find all cells where water can reach both
# the Pacific (top/left edges) and Atlantic (bottom/right edges).
#
# Constraints:
#   - m == len(heights), n == len(heights[0])
#   - 1 <= m, n <= 200
#   - 0 <= heights[i][j] <= 10^5
#
# Examples:
#   Input:  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
#   Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# ============================================================

def pacific_atlantic(heights):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
result = pacific_atlantic(heights)
expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
assert sorted(result) == sorted(expected)
print("All test cases passed!")
