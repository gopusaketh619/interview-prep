# ============================================================
# PROBLEM: 01 Matrix
# LeetCode: 542 | https://leetcode.com/problems/01-matrix/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given an m x n binary matrix mat, return the distance of
# the nearest 0 for each cell. The distance between two adjacent
# cells is 1.
#
# Constraints:
#   - m == len(mat), n == len(mat[0])
#   - 1 <= m, n <= 10^4
#   - 1 <= m * n <= 10^4
#   - mat[i][j] is either 0 or 1
#   - There is at least one 0 in mat
#
# Examples:
#   Input:  mat = [[0,0,0],[0,1,0],[0,0,0]]
#   Output: [[0,0,0],[0,1,0],[0,0,0]]
#
#   Input:  mat = [[0,0,0],[0,1,0],[1,1,1]]
#   Output: [[0,0,0],[0,1,0],[1,2,1]]
# ============================================================

def update_matrix(mat):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert update_matrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]]
assert update_matrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
print("All test cases passed!")
