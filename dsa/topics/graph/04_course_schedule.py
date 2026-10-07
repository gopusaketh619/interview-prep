# ============================================================
# PROBLEM: Course Schedule
# LeetCode: 207 | https://leetcode.com/problems/course-schedule/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# There are numCourses courses labeled 0 to numCourses - 1.
# Given prerequisites[i] = [a, b] meaning you must take b before a,
# return true if you can finish all courses (no cycle in DAG).
#
# Constraints:
#   - 1 <= numCourses <= 2000
#   - 0 <= len(prerequisites) <= 5000
#   - prerequisites[i].length == 2
#   - 0 <= a, b < numCourses
#
# Examples:
#   Input:  numCourses = 2, prerequisites = [[1,0]]
#   Output: True
#
#   Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
#   Output: False (cycle)
# ============================================================

from collections import deque, defaultdict


def can_finish(num_courses, prerequisites):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert can_finish(2, [[1, 0]]) == True
assert can_finish(2, [[1, 0], [0, 1]]) == False
assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) == True
assert can_finish(1, []) == True
print("All test cases passed!")
