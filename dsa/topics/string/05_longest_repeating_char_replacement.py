# ============================================================
# PROBLEM: Longest Repeating Character Replacement
# LeetCode: 424 | https://leetcode.com/problems/longest-repeating-character-replacement/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# You are given a string s and an integer k. You can choose any
# character and change it to any other uppercase English letter.
# You can perform this at most k times. Return the length of the
# longest substring containing the same letter after replacements.
#
# Constraints:
#   - 1 <= len(s) <= 10^5
#   - s consists of only uppercase English letters
#   - 0 <= k <= len(s)
#
# Examples:
#   Input:  s = "ABAB", k = 2
#   Output: 4 (replace both A's or both B's)
#
#   Input:  s = "AABABBA", k = 1
#   Output: 4
# ============================================================

def character_replacement(s, k):
    # Pattern: Variable-size sliding window + frequency map
    # Time: O(n * 26) → O(n) | Space: O(26) → O(1)
    #
    # Approach:
    #   1. Expand window by moving right pointer, tracking char frequencies.
    #   2. Window is valid when: window_size - max_freq <= k
    #      (i.e., the chars we'd need to replace fit within k).
    #   3. If invalid, shrink from left until valid again.
    #   4. Track the longest valid window seen.
    #
    # Key insight: In any window, keep the most frequent character and
    # replace the rest. If replacements needed > k, the window is too big.

    whm = {}
    max_len = 0
    left = 0

    for right in range(len(s)):
        whm[s[right]] = whm.get(s[right], 0) + 1

        # Shrink window while replacements needed exceed k
        while (right - left + 1) - max(whm.values()) > k:
            whm[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)
    return max_len


# --- Test Cases ---
assert character_replacement("ABAB", 2) == 4
assert character_replacement("AABABBA", 1) == 4
assert character_replacement("AAAA", 0) == 4
assert character_replacement("ABCD", 0) == 1
assert character_replacement("", 2) == 0
print("All test cases passed!")
