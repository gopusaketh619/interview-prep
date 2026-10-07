# ============================================================
# PROBLEM: Evaluate Reverse Polish Notation
# LeetCode: 150 | https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# You are given an array of strings tokens that represents
# an arithmetic expression in Reverse Polish Notation (postfix).
# Evaluate the expression and return the integer result.
# Valid operators are +, -, *, /. Division truncates toward zero.
#
# Constraints:
#   - 1 <= len(tokens) <= 10^4
#   - tokens[i] is either an operator or an integer in range [-200, 200]
#
# Examples:
#   Input:  tokens = ["2","1","+","3","*"]
#   Output: 9
#   Explanation: ((2 + 1) * 3) = 9
#
#   Input:  tokens = ["4","13","5","/","+"]
#   Output: 6
# ============================================================

def eval_rpn(tokens):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
assert eval_rpn(["3", "4", "+"]) == 7
print("All test cases passed!")
