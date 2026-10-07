# ============================================================
# PROBLEM: Permutations
# LeetCode: 46 | https://leetcode.com/problems/permutations/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array nums of distinct integers, return all possible
# permutations. You can return the answer in any order.
#
# Constraints:
#   - 1 <= len(nums) <= 6
#   - -10 <= nums[i] <= 10
#   - All integers of nums are unique
#
# Examples:
#   Input:  nums = [1, 2, 3]
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# ============================================================


from turtle import back


def permute(nums):
    # Pattern: Backtracking — try all items, skip already-used ones
    # Time: O(n * n!) | Space: O(n) recursion depth
    #
    # Approach:
    #   1. Loop over ALL indices (start from 0 every time — order matters)
    #   2. Skip already-used items via used[] array
    #   3. Base case: path length == nums length → save a copy
    result = []
    used = [False] * len(nums)

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], used)
    return result




# --- Test Cases ---
result = permute([1, 2, 3])
expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
assert sorted(result) == sorted(expected)

result = permute([0, 1])
assert sorted(result) == sorted([[0, 1], [1, 0]])

assert permute([1]) == [[1]]
print("All test cases passed!")
