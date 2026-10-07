# ============================================================
# PROBLEM: Longest Substring with At Most K Distinct Characters
# LeetCode: 340 | https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given a string s and an integer k, find the length of the 
# longest substring that contains at most k distinct characters.
#
# Constraints:
#   - 0 <= len(s) <= 5 * 10^4
#   - 0 <= k <= 50
#   - s consists of lowercase English letters
#
# Examples:
#   Input:  s = "eceba", k = 2
#   Output: 3
#   Explanation: "ece" has length 3 with 2 distinct characters
#
#   Input:  s = "aa", k = 1
#   Output: 2
#
#   Input:  s = "aabbcc", k = 3
#   Output: 6
#
#   Input:  s = "abcdef", k = 1
#   Output: 1
# ============================================================

# brute force
#def longest_substr_k_distinct(s, k):
#    max_len = 0
#    for i in range(len(s)):
#        for j in range(i+1, len(s)+1):
#            word = s[i:j]
#            if len(set(word)) == k:
#                max_len = max(max_len, len(word))
#    return max_len 


def longest_substr_k_distinct(s, k):
    # Pattern: Variable-size sliding window + frequency hashmap
    # Time: O(n) — each element added/removed at most once
    # Space: O(k) — hashmap holds at most k+1 keys before shrinking
    #
    # Approach:
    #   1. Expand window by adding s[right] to frequency map.
    #   2. Shrink from left while the window has more than k distinct chars.
    #   3. Update max_len with current valid window size.
    #
    # Generalization of "longest substring without repeats" (problem #5):
    #   #5 shrinks when any char count > 1 (i.e., k = all unique)
    #   #6 shrinks when distinct char count > k

    max_len = 0
    hm = {}      # char → frequency in current window
    left = 0

    for right in range(len(s)):
        # Expand: add right char to frequency map
        hm[s[right]] = hm.get(s[right], 0) + 1
        # Shrink: while more than k distinct chars, remove from left
        while len(hm) > k:
            hm[s[left]] -= 1
            if hm[s[left]] == 0:
                hm.pop(s[left])  # remove key entirely to keep len(hm) accurate
            left += 1
        # Update: window [left..right] is valid, track max size
        max_len = max(max_len, right - left + 1)
    return max_len


# --- Test Cases ---
assert longest_substr_k_distinct("eceba", 2) == 3
assert longest_substr_k_distinct("aa", 1) == 2
assert longest_substr_k_distinct("aabbcc", 3) == 6
assert longest_substr_k_distinct("abcdef", 1) == 1
assert longest_substr_k_distinct("", 2) == 0
assert longest_substr_k_distinct("abc", 0) == 0
print("All test cases passed!")
