# ============================================================
# PROBLEM: Combination Sum
# LeetCode: 39 | https://leetcode.com/problems/combination-sum/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of distinct integers candidates and a target,
# return a list of all unique combinations of candidates where
# the chosen numbers sum to target. The same number may be chosen
# an unlimited number of times.
#
# Constraints:
#   - 1 <= len(candidates) <= 30
#   - 2 <= candidates[i] <= 40
#   - All elements of candidates are distinct
#   - 1 <= target <= 40
#
# Examples:
#   Input:  candidates = [2,3,6,7], target = 7
#   Output: [[2,2,3],[7]]
# ============================================================

def combination_sum(candidates, target):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
result = combination_sum([2, 3, 6, 7], 7)
expected = sorted([sorted(x) for x in [[2, 2, 3], [7]]])
assert sorted([sorted(x) for x in result]) == expected

result = combination_sum([2, 3, 5], 8)
expected = sorted([sorted(x) for x in [[2, 2, 2, 2], [2, 3, 3], [3, 5]]])
assert sorted([sorted(x) for x in result]) == expected

assert combination_sum([2], 1) == []
print("All test cases passed!")
