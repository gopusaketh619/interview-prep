# ============================================================
# PROBLEM: Ransom Note
# LeetCode: 383 | https://leetcode.com/problems/ransom-note/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given two strings ransomNote and magazine, return true if
# ransomNote can be constructed from the letters in magazine.
# Each letter in magazine can only be used once.
#
# Constraints:
#   - 1 <= len(ransomNote), len(magazine) <= 10^5
#   - ransomNote and magazine consist of lowercase English letters
#
# Examples:
#   Input:  ransomNote = "a", magazine = "b"
#   Output: False
#
#   Input:  ransomNote = "aa", magazine = "aab"
#   Output: True
# ============================================================

from collections import Counter


def can_construct(ransom_note, magazine):
    # Pattern: Frequency count — compare letter availability
    # Time: O(n + m) | Space: O(1) — at most 26 lowercase letter keys
    #
    # Approach:
    #   1. Count letter frequencies in both strings using Counter.
    #   2. For each letter in ransom_note, check that magazine has
    #      at least as many copies.
    #   3. If any letter is missing or insufficient → False.

    ransom_hm = Counter(ransom_note)
    magazine_hm = Counter(magazine)

    for k in ransom_hm:
        if ransom_hm[k] > magazine_hm[k]:
            return False
    return True



# --- Test Cases ---
assert can_construct("a", "b") == False
assert can_construct("aa", "ab") == False
assert can_construct("aa", "aab") == True
assert can_construct("", "anything") == True
assert can_construct("abc", "abcdef") == True
print("All test cases passed!")
