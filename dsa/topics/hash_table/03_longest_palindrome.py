# ============================================================
# PROBLEM: Longest Palindrome
# LeetCode: 409 | https://leetcode.com/problems/longest-palindrome/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given a string s (mix of uppercase and lowercase), return the
# length of the longest palindrome that can be built with those letters.
#
# Constraints:
#   - 1 <= len(s) <= 2000
#   - s consists of lowercase and/or uppercase English letters
#
# Examples:
#   Input:  s = "abccccdd"
#   Output: 7
#   Explanation: "dccaccd" is one longest palindrome
#
#   Input:  s = "a"
#   Output: 1
# ============================================================

from collections import Counter


def longest_palindrome(s):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert longest_palindrome("abccccdd") == 7
assert longest_palindrome("a") == 1
assert longest_palindrome("Aa") == 1
assert longest_palindrome("aabbcc") == 6
assert longest_palindrome("bananas") == 5
print("All test cases passed!")
