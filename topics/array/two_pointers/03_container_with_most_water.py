# ============================================================
# PROBLEM: Container With Most Water
# LeetCode: 11 | https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given n non-negative integers representing heights of vertical 
# lines, find two lines that together with the x-axis form a 
# container that holds the most water.
#
# Return the maximum amount of water a container can store.
# (You may not slant the container.)
#
# Constraints:
#   - 2 <= len(height) <= 10^5
#   - 0 <= height[i] <= 10^4
#
# Examples:
#   Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
#   Explanation: Lines at index 1 (h=8) and index 8 (h=7)
#               Area = min(8,7) * (8-1) = 7 * 7 = 49
#
#   Input:  height = [1, 1]
#   Output: 1
#
#   Input:  height = [4, 3, 2, 1, 4]
#   Output: 16
# ============================================================


def max_area(height):
    # Pattern: Two pointers from both ends, shrink inward
    # Time: O(n) | Space: O(1)
    #
    # Approach:
    #   1. Start with the widest container (left=0, right=end).
    #   2. Compute area = min(height[L], height[R]) × (R - L).
    #   3. Move the pointer with the shorter height inward.
    #
    # Key insight: Moving the shorter pointer is the only way to
    # potentially find a taller line. Moving the taller pointer
    # can never help — the area is still capped by the shorter side,
    # and the width just got smaller.

    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(area, max_area)
        # Move the shorter side inward — only chance to increase area
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# --- Test Cases ---
assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_area([1, 1]) == 1
assert max_area([4, 3, 2, 1, 4]) == 16
assert max_area([1, 2, 1]) == 2
print("All test cases passed!")
