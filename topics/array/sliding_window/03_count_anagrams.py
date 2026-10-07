# ============================================================
# PROBLEM: Count Occurrences of Anagrams
# LeetCode: 438 | https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given a string s and a pattern p, find the number of 
# substrings in s that are anagrams of p.
#
# Two strings are anagrams if they contain the same characters 
# with the same frequencies, regardless of order.
#
# Constraints:
#   - 1 <= len(p) <= len(s) <= 10^5
#   - s and p consist of lowercase English letters
#
# Examples:
#   Input:  s = "cbaebabacd", p = "abc"
#   Output: 2
#   Explanation: "cba" (index 0) and "bac" (index 6)
#
#   Input:  s = "abab", p = "ab"
#   Output: 3
#   Explanation: "ab" (index 0), "ba" (index 1), "ab" (index 2)
#
#   Input:  s = "aaaa", p = "aa"
#   Output: 3
# ============================================================

def build_hm(hm, e, task):
    if task == 'add':
        if e not in hm.keys():
            hm[e] = 1
        else:
            hm[e] += 1
    elif task == 'remove':
        hm[e] -= 1
        if hm[e] == 0:
            hm.pop(e)
    else:
        raise 
    return hm
            


def count_anagrams(s, p):
    # Pattern: Fixed-size sliding window + two frequency maps comparison
    # Time: O(n * 26) ≈ O(n) | Space: O(1) — at most 26 keys per map
    #
    # Approach:
    #   1. Build a frequency map for pattern p.
    #   2. Slide a window of size len(p) over s, maintaining a window freq map.
    #   3. At each valid window position, compare the two maps directly.
    #      If they're equal, the window is an anagram of p.

    s_len = len(s)
    p_len = len(p)
    result = 0

    # Build frequency map for pattern
    p_hm = {}
    s_hm = {}
    for c in p:
        build_hm(p_hm, c, 'add')
    
    left = 0
    for right in range(s_len):
        if right < p_len - 1:
            # Still building the first window (not yet full size)
            build_hm(s_hm, s[right], 'add')
        else:
            # Expand: add right char to window
            build_hm(s_hm, s[right], 'add')
            # Shrink: remove left char if window exceeds size p_len
            if left < right - p_len + 1:
                build_hm(s_hm, s[left], 'remove')
                left += 1
            # Check: if both freq maps match, it's an anagram
            if p_hm == s_hm:
                result += 1
    return result


def count_anagrams_opt(s, p):
    # Pattern: Fixed-size sliding window + match counter
    # Time: O(n) — true O(1) per iteration (int comparison, not dict comparison)
    # Space: O(1) — at most 26 keys in each map
    #
    # Approach:
    #   1. Build a frequency map of pattern p.
    #   2. Slide a window of size len(p) over s.
    #   3. Instead of comparing two dicts each time, track how many
    #      distinct characters are fully "matched" (window freq == pattern freq).
    #   4. When matched == number of distinct chars in p, the window is an anagram.

    from collections import Counter

    p_map = Counter(p)
    s_len, p_len = len(s), len(p)
    needed = len(p_map)   # number of distinct chars we need to satisfy
    matched = 0           # how many distinct chars currently have exact freq match
    window = {}
    result = 0

    for right in range(s_len):
        # Expand: add right char to window
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1
        # If this char is in pattern and freqs now match, increment matched
        if ch in p_map and window[ch] == p_map[ch]:
            matched += 1

        # Shrink: remove leftmost char when window exceeds size p_len
        if right >= p_len:
            left_ch = s[right - p_len]
            # If removing this char breaks an exact match, decrement matched
            if left_ch in p_map and window[left_ch] == p_map[left_ch]:
                matched -= 1
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]

        # Check: all distinct chars satisfied → window is an anagram
        if matched == needed:
            result += 1

    return result


# --- Test Cases ---
assert count_anagrams("cbaebabacd", "abc") == 2
assert count_anagrams("abab", "ab") == 3
assert count_anagrams("aaaa", "aa") == 3
assert count_anagrams("abcd", "xyz") == 0

assert count_anagrams_opt("cbaebabacd", "abc") == 2
assert count_anagrams_opt("abab", "ab") == 3
assert count_anagrams_opt("aaaa", "aa") == 3
assert count_anagrams_opt("abcd", "xyz") == 0
print("All test cases passed!")
