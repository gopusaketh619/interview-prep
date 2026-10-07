# ============================================================
# PROBLEM: Number of Islands
# LeetCode: 200 | https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an m x n 2D grid of '1's (land) and '0's (water),
# return the number of islands. An island is surrounded by
# water and formed by connecting adjacent lands horizontally
# or vertically.
#
# Constraints:
#   - m == len(grid), n == len(grid[0])
#   - 1 <= m, n <= 300
#   - grid[i][j] is '0' or '1'
#
# Examples:
#   Input:  grid = [["1","1","0"],["1","1","0"],["0","0","1"]]
#   Output: 2
# ============================================================

def num_islands(grid):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
assert num_islands(grid1) == 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
assert num_islands(grid2) == 3

assert num_islands([]) == 0
print("All test cases passed!")
