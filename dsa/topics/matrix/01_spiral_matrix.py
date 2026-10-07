# ============================================================
# PROBLEM: Spiral Matrix
# LeetCode: 54 | https://leetcode.com/problems/spiral-matrix/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an m x n matrix, return all elements of the matrix
# in spiral order.
#
# Constraints:
#   - m == len(matrix), n == len(matrix[0])
#   - 1 <= m, n <= 10
#   - -100 <= matrix[i][j] <= 100
#
# Examples:
#   Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
#   Output: [1,2,3,6,9,8,7,4,5]
# ============================================================

def spiral_order(matrix):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
assert spiral_order([[1]]) == [1]
assert spiral_order([[1,2],[3,4]]) == [1,2,4,3]
print("All test cases passed!")
