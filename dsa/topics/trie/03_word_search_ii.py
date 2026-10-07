# ============================================================
# PROBLEM: Word Search II
# LeetCode: 212 | https://leetcode.com/problems/word-search-ii/
# Difficulty: Hard | Time to Solve: 35 min
# ============================================================
# Given an m x n board of characters and a list of strings words,
# return all words on the board. Each word must be constructed
# from sequentially adjacent cells, where adjacent cells are
# horizontal or vertical neighbors.
#
# Constraints:
#   - m == len(board), n == len(board[0])
#   - 1 <= m, n <= 12
#   - 1 <= len(words) <= 3 * 10^4
#   - 1 <= len(words[i]) <= 10
#
# Examples:
#   Input:  board = [["o","a","a","n"],["e","t","a","e"]], words = ["oath","eat","rain"]
#   Output: ["eat","oath"]
# ============================================================

def find_words(board, words):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
assert sorted(find_words(board, words)) == sorted(["eat","oath"])
print("All test cases passed!")
