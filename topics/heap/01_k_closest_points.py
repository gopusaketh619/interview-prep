# ============================================================
# PROBLEM: K Closest Points to Origin
# LeetCode: 973 | https://leetcode.com/problems/k-closest-points-to-origin/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of points where points[i] = [xi, yi] represents
# a point on the X-Y plane and an integer k, return the k closest
# points to the origin (0, 0).
#
# Constraints:
#   - 1 <= k <= len(points) <= 10^4
#   - -10^4 <= xi, yi <= 10^4
#
# Examples:
#   Input:  points = [[1,3],[-2,2]], k = 1
#   Output: [[-2,2]]
#   Explanation: dist(1,3) = sqrt(10), dist(-2,2) = sqrt(8)
# ============================================================

import heapq


def k_closest(points, k):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def k_closest_sort(points, k):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
result = k_closest([[1, 3], [-2, 2]], 1)
assert result == [[-2, 2]]

result = k_closest([[3, 3], [5, -1], [-2, 4]], 2)
result_sorted = sorted(result)
assert sorted(result_sorted) == sorted([[3, 3], [-2, 4]])

print("All test cases passed!")
