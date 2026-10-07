# ============================================================
# PROBLEM: Word Break
# LeetCode: 139 | https://leetcode.com/problems/word-break/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given a string s and a dictionary of strings wordDict, return
# true if s can be segmented into a space-separated sequence
# of one or more dictionary words.
#
# Constraints:
#   - 1 <= len(s) <= 300
#   - 1 <= len(wordDict) <= 1000
#   - 1 <= len(wordDict[i]) <= 20
#   - s and wordDict[i] consist of only lowercase English letters
#
# Examples:
#   Input:  s = "leetcode", wordDict = ["leet","code"]
#   Output: True
#
#   Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#   Output: False
# ============================================================

def word_break(s, word_dict):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert word_break("leetcode", ["leet", "code"]) == True
assert word_break("applepenapple", ["apple", "pen"]) == True
assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
print("All test cases passed!")
