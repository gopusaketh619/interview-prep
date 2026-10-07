# ============================================================
# PROBLEM: Pow(x, n)
# LeetCode: 50 | https://leetcode.com/problems/powx-n/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Implement pow(x, n), which calculates x raised to the
# power n (i.e., x^n).
#
# Constraints:
#   - -100.0 < x < 100.0
#   - -2^31 <= n <= 2^31 - 1
#   - n is an integer
#   - x is not zero when n < 0
#
# Examples:
#   Input:  x = 2.0, n = 10
#   Output: 1024.0
#
#   Input:  x = 2.0, n = -2
#   Output: 0.25 (i.e., 2^-2 = 1/4)
# ============================================================

def my_pow(x, n):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert abs(my_pow(2.0, 10) - 1024.0) < 1e-6
assert abs(my_pow(2.1, 3) - 9.261) < 1e-3
assert abs(my_pow(2.0, -2) - 0.25) < 1e-6
print("All test cases passed!")
