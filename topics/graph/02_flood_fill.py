# ============================================================
# PROBLEM: Flood Fill
# LeetCode: 733 | https://leetcode.com/problems/flood-fill/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# An image is represented by an m x n grid of integers. Given
# a starting pixel (sr, sc) and a color, perform a flood fill
# on the image starting from that pixel.
#
# Constraints:
#   - m == len(image), n == len(image[0])
#   - 1 <= m, n <= 50
#   - 0 <= image[i][j], color < 2^16
#
# Examples:
#   Input:  image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#   Output: [[2,2,2],[2,2,0],[2,0,1]]
# ============================================================

def flood_fill(image, sr, sc, color):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
assert flood_fill([[0,0,0],[0,0,0]], 0, 0, 0) == [[0,0,0],[0,0,0]]
assert flood_fill([[0,0,0],[0,1,1]], 1, 1, 1) == [[0,0,0],[0,1,1]]
print("All test cases passed!")
