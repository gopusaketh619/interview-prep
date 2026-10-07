# ============================================================
# PROBLEM: Word Search
# LeetCode: 79 | https://leetcode.com/problems/word-search/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given an m x n grid of characters board and a string word,
# return true if word can be found in the grid. The word can
# be constructed from sequentially adjacent cells (horizontal
# or vertical). Each cell may be used at most once.
#
# Constraints:
#   - m == len(board), n == len(board[0])
#   - 1 <= m, n <= 6
#   - 1 <= len(word) <= 15
#   - board and word consist of only English letters
#
# Examples:
#   Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#   Output: True
# ============================================================

def exist(board, word):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
assert exist(board, "ABCCED") == True
assert exist(board, "SEE") == True
assert exist(board, "ABCB") == False
print("All test cases passed!")
