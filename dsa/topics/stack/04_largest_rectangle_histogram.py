# ============================================================
# PROBLEM: Largest Rectangle in Histogram
# LeetCode: 84 | https://leetcode.com/problems/largest-rectangle-in-histogram/
# Difficulty: Hard | Time to Solve: 35 min
# ============================================================
# Given an array of integers heights representing the histogram's
# bar height where the width of each bar is 1, return the area
# of the largest rectangle in the histogram.
#
# Constraints:
#   - 1 <= len(heights) <= 10^5
#   - 0 <= heights[i] <= 10^4
#
# Examples:
#   Input:  heights = [2, 1, 5, 6, 2, 3]
#   Output: 10
#   Explanation: 5 and 6 bars form a rectangle of area 5*2 = 10
#
#   Input:  heights = [2, 4]
#   Output: 4
# ============================================================

def largest_rectangle_brute(heights):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def largest_rectangle(heights):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle([2, 4]) == 4
assert largest_rectangle([1]) == 1
assert largest_rectangle([1, 1, 1, 1]) == 4
assert largest_rectangle_brute([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle_brute([2, 4]) == 4
assert largest_rectangle_brute([1]) == 1
assert largest_rectangle_brute([1, 1, 1, 1]) == 4
print("All test cases passed!")
