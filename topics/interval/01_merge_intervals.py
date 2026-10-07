# ============================================================
# PROBLEM: Merge Intervals
# LeetCode: 56 | https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of intervals where intervals[i] = [start, end],
# merge all overlapping intervals, and return an array of the
# non-overlapping intervals that cover all the input intervals.
#
# Constraints:
#   - 1 <= len(intervals) <= 10^4
#   - intervals[i].length == 2
#   - 0 <= start <= end <= 10^4
#
# Examples:
#   Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#
#   Input:  intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
# ============================================================

def merge(intervals):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert merge([[1,4],[4,5]]) == [[1,5]]
assert merge([[1,4],[0,4]]) == [[0,4]]
assert merge([[1,4]]) == [[1,4]]
print("All test cases passed!")
