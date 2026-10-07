# ============================================================
# PROBLEM: Insert Interval
# LeetCode: 57 | https://leetcode.com/problems/insert-interval/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# You are given an array of non-overlapping intervals sorted by
# start time, and a new interval. Insert the new interval and
# merge if necessary. Return the resulting sorted intervals.
#
# Constraints:
#   - 0 <= len(intervals) <= 10^4
#   - intervals[i].length == 2
#   - 0 <= start <= end <= 10^5
#   - intervals is sorted by start in ascending order
#
# Examples:
#   Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
#   Output: [[1,5],[6,9]]
#
#   Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#   Output: [[1,2],[3,10],[12,16]]
# ============================================================

def insert(intervals, new_interval):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
assert insert([], [5,7]) == [[5,7]]
assert insert([[1,5]], [2,3]) == [[1,5]]
print("All test cases passed!")
