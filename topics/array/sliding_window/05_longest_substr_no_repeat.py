# ============================================================
# PROBLEM: Longest Substring Without Repeating Characters
# LeetCode: 3 | https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given a string s, find the length of the longest substring 
# that contains no repeating characters.
#
# Constraints:
#   - 0 <= len(s) <= 5 * 10^4
#   - s consists of English letters, digits, symbols, and spaces
#
# Examples:
#   Input:  s = "abcabcbb"
#   Output: 3
#   Explanation: "abc" has length 3
#
#   Input:  s = "bbbbb"
#   Output: 1
#   Explanation: "b" has length 1
#
#   Input:  s = "pwwkew"
#   Output: 3
#   Explanation: "wke" has length 3
#
#   Input:  s = ""
#   Output: 0
# ============================================================

from collections import Counter, deque

def longest_substring_no_repeat(s):
    # Pattern: Variable-size sliding window + last-seen-index map
    # Time: O(n) — single pass, left pointer only jumps forward
    # Space: O(min(n, 26)) = O(1) for lowercase letters
    #
    # Approach:
    #   1. Store the last seen index of each character.
    #   2. When a duplicate is found WITHIN the current window,
    #      jump left directly past the previous occurrence.
    #   3. Track max window size (right - left + 1) at each step.
    #
    # Key insight: We check `last_seen[char] >= left` to ensure the
    # previous occurrence is inside the current window. If it's outside,
    # we ignore it (prevents left from moving backwards).

    max_len = 0
    last_seen = {}   # char → most recent index where it appeared
    left = 0

    for right in range(len(s)):
        # If char seen before AND its last position is within our window
        if s[right] in last_seen and last_seen[s[right]] >= left:
            # Jump left past the duplicate (skip the while loop shrinking)
            left = last_seen[s[right]] + 1
        # Always update the last seen position
        last_seen[s[right]] = right
        # Update answer: current window length = right - left + 1
        max_len = max(max_len, right-left+1)
    return max_len
    
    

# --- Test Cases ---
assert longest_substring_no_repeat("abcabcbb") == 3
assert longest_substring_no_repeat("bbbbb") == 1
assert longest_substring_no_repeat("pwwkew") == 3
assert longest_substring_no_repeat("") == 0
assert longest_substring_no_repeat("abcdef") == 6
assert longest_substring_no_repeat(" ") == 1
print("All test cases passed!")
