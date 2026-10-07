# ============================================================
# PROBLEM: Minimum Window Substring (Hard)
# LeetCode: 76 | https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard | Time to Solve: 30 min
# ============================================================
# Given two strings s and t, return the minimum window 
# substring of s that contains ALL characters of t (including 
# duplicates). If no such substring exists, return "".
#
# The answer is guaranteed to be unique if it exists.
#
# Constraints:
#   - 1 <= len(s), len(t) <= 10^5
#   - s and t consist of uppercase and lowercase English letters
#
# Follow-up: Can you solve it in O(n) time?
#
# Examples:
#   Input:  s = "ADOBECODEBANC", t = "ABC"
#   Output: "BANC"
#   Explanation: "BANC" is the smallest window containing A, B, C
#
#   Input:  s = "a", t = "a"
#   Output: "a"
#
#   Input:  s = "a", t = "aa"
#   Output: ""
#   Explanation: Both 'a's are required but s has only one
#
#   Input:  s = "cjabwefgewcwaefgcf", t = "cae"
#   Output: "cwae"
# ============================================================

from collections import Counter

def min_window_substring(s, t):
    # Pattern: Variable-size sliding window + match counter
    # Time: O(n) — each element visited at most twice (once by right, once by left)
    # Space: O(1) — at most 52 keys (uppercase + lowercase English letters)
    #
    # Key difference from previous problems:
    #   Previous (#5,#6,#7,#8): shrink while window is INVALID → find LONGEST
    #   This problem:           shrink while window is VALID   → find SHORTEST
    #
    # Approach:
    #   1. Build frequency map of t (what we need).
    #   2. Expand right — track how many distinct chars are fully satisfied.
    #   3. While all chars satisfied (matched == required):
    #      - Record current window if it's the smallest seen
    #      - Shrink from left to try finding a smaller valid window
    #   4. Return the smallest valid window found.

    t_map = Counter(t)
    min_len = float('inf')
    min_start = 0
    left = 0
    # required = number of distinct chars in t that need to be satisfied
    required = len(t_map)
    matched = 0              # distinct chars currently fully satisfied
    window_hm = {}

    for right in range(len(s)):
        # Expand: add right char to window
        r_ch = s[right]
        window_hm[r_ch] = window_hm.get(r_ch, 0) + 1

        # If this char is in t and its count just reached the target, it's satisfied
        if r_ch in t_map and window_hm[r_ch] == t_map[r_ch]:
            matched += 1

        # Shrink: while window is valid, try to minimize it
        while matched == required:
            # Update answer if current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            # Remove left char from window
            l_ch = s[left]
            # Check BEFORE decrement: if removing this breaks a satisfied char
            if l_ch in t_map and window_hm[l_ch] == t_map[l_ch]:
                matched -= 1
            window_hm[l_ch] -= 1
            if window_hm[l_ch] == 0:
                del window_hm[l_ch]
            left += 1

    # Slice only once at the end using tracked indices
    return s[min_start:min_start + min_len] if min_len != float('inf') else ''



# --- Test Cases ---
assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
assert min_window_substring("a", "a") == "a"
assert min_window_substring("a", "aa") == ""
assert min_window_substring("cabwefgewcwaefgcf", "cae") == "cwae"
assert min_window_substring("abc", "d") == ""
print("All test cases passed!")
