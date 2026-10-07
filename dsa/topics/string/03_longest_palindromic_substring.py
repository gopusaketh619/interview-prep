# ============================================================
# PROBLEM: Longest Palindromic Substring
# LeetCode: 5 | https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given a string s, return the longest palindromic substring in s.
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

def longest_palindrome_brute(s):
    # Pattern: Brute force — check every substring
    # Time: O(n^3) | Space: O(n)
    #
    # Approach:
    #   1. Try every substring s[i:j].
    #   2. Check if it's a palindrome (compare with its reverse).
    #   3. Keep the longest palindrome found.

    best = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
    return best

def expand_from_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]


def longest_palindrome(s):
    # Pattern: Expand around center
    # Time: O(n^2) | Space: O(1) excluding output
    #
    # Approach:
    #   1. Every palindrome has a center. Try each index as center.
    #   2. Expand outward from (i, i) for odd-length palindromes.
    #   3. Expand outward from (i, i+1) for even-length palindromes.
    #   4. Keep the longest palindrome found.
    #
    # Key insight: Instead of checking all O(n^2) substrings,
    # we only expand from n centers — each expansion stops early
    # when characters mismatch.

    best = ""
    for i in range(len(s)):
        odd = expand_from_center(s, i, i)
        even = expand_from_center(s, i, i + 1)
        pal = odd if len(odd) >= len(even) else even
        if len(pal) > len(best):
            best = pal
    return best


# --- Test Cases ---
assert longest_palindrome_brute("babad") in ("bab", "aba")
assert longest_palindrome_brute("cbbd") == "bb"
assert longest_palindrome_brute("a") == "a"
assert longest_palindrome_brute("ac") in ("a", "c")

assert longest_palindrome("babad") in ("bab", "aba")
assert longest_palindrome("cbbd") == "bb"
assert longest_palindrome("a") == "a"
assert longest_palindrome("ac") in ("a", "c")
assert longest_palindrome("aaabb") == "aaa"
print("All test cases passed!")
