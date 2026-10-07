# ============================================================
# PROBLEM: Subsets II
# LeetCode: 90 | https://leetcode.com/problems/subsets-ii/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an integer array nums that may contain duplicates,
# return all possible subsets (the power set). The solution
# must not contain duplicate subsets.
#
# Constraints:
#   - 1 <= len(nums) <= 10
#   - -10 <= nums[i] <= 10
#
# Examples:
#   Input:  nums = [1, 2, 2]
#   Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# ============================================================


def subsets_with_dup(nums):
    # Pattern: Backtracking — Sort + skip duplicates at same level
    # Time: O(n * 2^n) | Space: O(n) recursion depth
    #
    # Approach:
    #   1. Sort so duplicates are adjacent
    #   2. At each node, save current path as a valid subset
    #   3. Loop from i onward, skip if same value already used at this level

    nums.sort()
    result = []

    def backtrack(i, path):
        result.append(path[:])

        for j in range(i, len(nums)):
            # Skip duplicate values at the same decision level
            if j > i and nums[j] == nums[j - 1]:
                continue
            path.append(nums[j])   # choose
            backtrack(j + 1, path) # explore
            path.pop()             # unchoose

    backtrack(0, [])
    return result


# --- Test Cases ---
result = subsets_with_dup([1, 2, 2])
assert len(result) == 6
print("All test cases passed!")
