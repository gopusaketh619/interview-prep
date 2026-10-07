# ============================================================
# PROBLEM: Non-overlapping Intervals
# LeetCode: 435 | https://leetcode.com/problems/non-overlapping-intervals/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of intervals where intervals[i] = [start, end],
# return the minimum number of intervals you need to REMOVE to 
# make the rest of the intervals non-overlapping.
#
# Constraints:
#   - 1 <= len(intervals) <= 10^5
#   - intervals[i].length == 2
#   - -5 * 10^4 <= start < end <= 5 * 10^4
#
# Examples:
#   Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
#   Output: 1
#   Explanation: Remove [1,3] to make the rest non-overlapping
#
#   Input:  intervals = [[1,2],[1,2],[1,2]]
#   Output: 2
#
#   Input:  intervals = [[1,2],[2,3]]
#   Output: 0
#
# Hint: Sort by end time. Greedily keep intervals that end earliest.
# ============================================================


def erase_overlap_intervals(intervals):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert erase_overlap_intervals([[1,2],[1,2],[1,2]]) == 2
assert erase_overlap_intervals([[1,2],[2,3]]) == 0
assert erase_overlap_intervals([[1,100],[11,22],[1,11],[2,12]]) == 2
print("All test cases passed!")
