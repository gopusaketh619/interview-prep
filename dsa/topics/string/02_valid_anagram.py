# ============================================================
# PROBLEM: Valid Anagram
# LeetCode: 242 | https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given two strings s and t, return true if t is an anagram
# of s, and false otherwise. An anagram uses all the original
# letters exactly once.
#
# Constraints:
#   - 1 <= len(s), len(t) <= 5 * 10^4
#   - s and t consist of lowercase English letters
#
# Examples:
#   Input:  s = "anagram", t = "nagaram"
#   Output: True
#
#   Input:  s = "rat", t = "car"
#   Output: False
# ============================================================

from collections import Counter

def is_anagram_sort(s, t):
    # Pattern: Sorting — anagrams become identical when sorted
    # Time: O(n log n) | Space: O(n) — sorted() creates new lists
    #
    # Approach:
    #   1. Sort both strings — anagrams will produce the same sequence.
    #   2. Compare the sorted results.

    return sorted(s) == sorted(t)


def is_anagram(s, t):
    # Pattern: Frequency count — compare character frequencies
    # Time: O(n) | Space: O(1) — at most 26 lowercase letter keys
    #
    # Approach:
    #   1. Build a frequency map for each string using Counter.
    #   2. If the maps are equal, every letter appears the same
    #      number of times → anagram.

    return Counter(s) == Counter(t)
    


# --- Test Cases ---
assert is_anagram("anagram", "nagaram") == True
assert is_anagram("rat", "car") == False
assert is_anagram("", "") == True
assert is_anagram("a", "ab") == False
assert is_anagram_sort("anagram", "nagaram") == True
assert is_anagram_sort("rat", "car") == False
print("All test cases passed!")
