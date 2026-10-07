# ============================================================
# PROBLEM: Merge Intervals
# LeetCode: 56 | https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of intervals where intervals[i] = [start, end],
# merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals.
#
# Constraints:
#   - 1 <= len(intervals) <= 10^4
#   - intervals[i].length == 2
#   - 0 <= start <= end <= 10^4
#
# Examples:
#   Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#   Explanation: [1,3] and [2,6] overlap → merge to [1,6]
#
#   Input:  intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
#
#   Input:  intervals = [[1,4],[0,4]]
#   Output: [[0,4]]
#
# Hint: Sort by start time, then iterate and merge overlaps.
# ============================================================


def merge_intervals(intervals):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
assert merge_intervals([[1,4],[0,4]]) == [[0,4]]
assert merge_intervals([[1,4],[2,3]]) == [[1,4]]
assert merge_intervals([[1,2]]) == [[1,2]]
print("All test cases passed!")
