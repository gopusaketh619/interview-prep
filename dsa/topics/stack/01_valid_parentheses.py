# ============================================================
# PROBLEM: Valid Parentheses
# LeetCode: 20 | https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the
# input string is valid.
# A string is valid if brackets are closed in the correct order
# and each close bracket has a corresponding open bracket.
#
# Constraints:
#   - 1 <= len(s) <= 10^4
#   - s consists of parentheses only '()[]{}'
#
# Examples:
#   Input:  s = "()"
#   Output: True
#
#   Input:  s = "([)]"
#   Output: False
#
#   Input:  s = "{[]}"
#   Output: True
# ============================================================

def is_valid(s):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert is_valid("()") == True
assert is_valid("()[]{}") == True
assert is_valid("(]") == False
assert is_valid("([)]") == False
assert is_valid("{[]}") == True
assert is_valid("") == True
assert is_valid("(") == False
print("All test cases passed!")
