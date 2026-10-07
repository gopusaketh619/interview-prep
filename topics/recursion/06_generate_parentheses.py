# ============================================================
# PROBLEM: Generate Parentheses
# LeetCode: 22 | https://leetcode.com/problems/generate-parentheses/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# Constraints:
#   - 1 <= n <= 8
#
# Examples:
#   Input:  n = 3
#   Output: ["((()))","(()())","(())()","()(())","()()()"]
#
#   Input:  n = 1
#   Output: ["()"]
# ============================================================

def generate_parenthesis(n):
    # Pattern: Backtracking with constraints
    # Time: O(4^n / sqrt(n)) — nth Catalan number | Space: O(n) recursion depth
    #
    # Approach:
    #   1. At each step, choose to add "(" or ")"
    #   2. Can add "(" only if open_count < n
    #   3. Can add ")" only if close_count < open_count
    #   4. Base case: string length == 2*n → valid result
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# --- Test Cases ---
assert sorted(generate_parenthesis(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
assert generate_parenthesis(1) == ["()"]
print("All test cases passed!")
