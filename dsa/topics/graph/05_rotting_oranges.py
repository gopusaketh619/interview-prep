# ============================================================
# PROBLEM: Rotting Oranges
# LeetCode: 994 | https://leetcode.com/problems/rotting-oranges/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# In a grid, 0 = empty, 1 = fresh orange, 2 = rotten orange.
# Every minute, fresh oranges adjacent (4-directional) to rotten
# ones become rotten. Return the minimum minutes until no fresh
# orange remains. If impossible, return -1.
#
# Constraints:
#   - m == len(grid), n == len(grid[0])
#   - 1 <= m, n <= 10
#   - grid[i][j] is 0, 1, or 2
#
# Examples:
#   Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
#   Output: 4
#
#   Input:  grid = [[2,1,1],[0,1,1],[1,0,1]]
#   Output: -1 (bottom-left unreachable)
# ============================================================

from collections import deque


def oranges_rotting(grid):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert oranges_rotting([[0,2]]) == 0
assert oranges_rotting([[0]]) == 0
print("All test cases passed!")
