# ============================================================
# PROBLEM: Word Ladder
# LeetCode: 127 | https://leetcode.com/problems/word-ladder/
# Difficulty: Hard | Time to Solve: 35 min
# ============================================================
# Given beginWord, endWord, and a wordList, find the length of
# the shortest transformation sequence from beginWord to endWord,
# such that only one letter can be changed at each step and each
# intermediate word must be in wordList. Return 0 if impossible.
#
# Constraints:
#   - 1 <= beginWord.length <= 10
#   - endWord.length == beginWord.length
#   - 1 <= len(wordList) <= 5000
#   - All words have the same length and consist of lowercase English letters
#
# Examples:
#   Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#   Output: 5 (hit -> hot -> dot -> dog -> cog)
# ============================================================

from collections import deque


def ladder_length(begin_word, end_word, word_list):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
assert ladder_length("a", "c", ["a","b","c"]) == 2
print("All test cases passed!")
