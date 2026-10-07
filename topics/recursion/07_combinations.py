# ============================================================
# PROBLEM: Combinations
# LeetCode: 77 | https://leetcode.com/problems/combinations/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given two integers n and k, return all possible combinations
# of k numbers chosen from the range [1, n].
#
# Constraints:
#   - 1 <= n <= 20
#   - 1 <= k <= n
#
# Examples:
#   Input:  n = 4, k = 2
#   Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# ============================================================

from turtle import back


def combine(n, k):
    # Pattern: Backtracking — Choose → Explore → Unchoose
    # Time: O(k * C(n,k)) | Space: O(k) recursion depth
    #
    # Approach:
    #   1. Pick numbers from start to n, always moving forward
    #   2. Base case: path has k elements → save a copy
    #   3. Choose (append) → Explore (recurse with i+1) → Unchoose (pop)
    result = []

    def backtrack(start, path):

        if len(path) == k:
            result.append(path[:])
            return 

        for i in range(start, n+1):
            path.append(i)
            backtrack(i+1, path)
            path.pop()

    backtrack(1, [])
    return result


# --- Test Cases ---
assert sorted(combine(4, 2)) == sorted([[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
assert combine(1, 1) == [[1]]
print("All test cases passed!")
