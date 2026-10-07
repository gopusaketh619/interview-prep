# ============================================================
# PROBLEM: Group Anagrams
# LeetCode: 49 | https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
#
# Constraints:
#   - 1 <= len(strs) <= 10^4
#   - 0 <= len(strs[i]) <= 100
#   - strs[i] consists of lowercase English letters
#
# Examples:
#   Input:  strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# ============================================================

from collections import defaultdict


def group_anagrams(strs):
    # Pattern: Brute force — compare every pair using sorted characters
    # Time: O(n^2 * m log m) | Space: O(n * m)
    #   n = number of strings, m = max string length
    #
    # Approach:
    #   1. For each string, skip if already grouped.
    #   2. Compare against every other string using sorted() to check anagram.
    #   3. Collect matches into a group and add to results.

    results = []
    tot = len(strs)
    for i in range(tot):
        if strs[i] in [s for sublist in results for s in sublist]:
            continue
        r = [strs[i]]
        for j in range(tot):
            if i != j and sorted(strs[i]) == sorted(strs[j]):
                r.append(strs[j])
        results.append(r)
    return results


def group_anagrams_count(strs):
    # Pattern: Character-count fingerprint as hashmap key
    # Time: O(n * m) | Space: O(n * m)
    #   n = number of strings, m = max string length
    #
    # Approach:
    #   1. For each string, build a 26-element count array (one slot per letter).
    #   2. Convert to tuple (hashable) and use as dict key.
    #   3. Anagrams produce the same count tuple → land in the same bucket.
    #   4. Return all buckets as the grouped result.
    #
    # Key insight: Avoids sorting (O(m log m)) by using O(m) counting instead.

    groups = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(s)

    return list(groups.values())



# --- Test Cases ---
result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
result_sorted = sorted([sorted(g) for g in result])
expected = sorted([sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]])
assert result_sorted == expected

result2 = group_anagrams_count(["eat", "tea", "tan", "ate", "nat", "bat"])
result2_sorted = sorted([sorted(g) for g in result2])
assert result2_sorted == expected

assert group_anagrams([""]) == [[""]]
assert group_anagrams(["a"]) == [["a"]]
print("All test cases passed!")
