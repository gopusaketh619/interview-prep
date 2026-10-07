# ============================================================
# PROBLEM: Longest Palindromic Substring (DP)
# LeetCode: 5 | https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given a string s, return the longest palindromic substring in s.
# This file uses a dynamic programming approach.
#
# Constraints:
#   - 1 <= len(s) <= 1000
#   - s consists of only digits and English letters
#
# Examples:
#   Input:  s = "babad"
#   Output: "bab" or "aba"
#
#   Input:  s = "cbbd"
#   Output: "bb"
# ============================================================

def longest_palindrome_dp(s):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert longest_palindrome_dp("babad") in ("bab", "aba")
assert longest_palindrome_dp("cbbd") == "bb"
assert longest_palindrome_dp("a") == "a"
print("All test cases passed!")
