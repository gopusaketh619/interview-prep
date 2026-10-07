# ============================================================
# PROBLEM: Subsets
# LeetCode: 78 | https://leetcode.com/problems/subsets/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an integer array nums of unique elements, return all
# possible subsets (the power set). The solution must not contain
# duplicate subsets.
#
# Constraints:
#   - 1 <= len(nums) <= 10
#   - -10 <= nums[i] <= 10
#   - All elements of nums are unique
#
# Examples:
#   Input:  nums = [1, 2, 3]
#   Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# ============================================================

def subsets(nums):
    # Pattern: Backtracking — Include/Exclude binary decision tree
    # Time: O(n * 2^n) | Space: O(n) recursion depth
    #
    # Approach:
    #   1. For each element, make a binary choice: exclude or include
    #   2. Base case: processed all elements (i == len) → save path copy
    #   3. Two branches per element → 2^n total subsets

    result = []

    def backtrack(i, path):
        if i == len(nums):
            result.append(path[:])
            return

        # Branch 1: Exclude nums[i]
        backtrack(i + 1, path)

        # Branch 2: Include nums[i] → choose, explore, unchoose
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()

    backtrack(0, [])
    return result




# --- Test Cases ---
result = subsets([1, 2, 3])
expected = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

result = subsets([0])
assert sorted([sorted(x) for x in result]) == sorted([[], [0]])
print("All test cases passed!")
