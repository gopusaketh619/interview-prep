# ============================================================
# PROBLEM: Task Scheduler
# LeetCode: 621 | https://leetcode.com/problems/task-scheduler/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given a char array tasks and a cooling interval n, find the
# minimum number of intervals the CPU needs to finish all tasks.
# Same tasks must be separated by at least n intervals.
#
# Constraints:
#   - 1 <= len(tasks) <= 10^4
#   - tasks[i] is uppercase English letter
#   - 0 <= n <= 100
#
# Examples:
#   Input:  tasks = ["A","A","A","B","B","B"], n = 2
#   Output: 8 (A -> B -> idle -> A -> B -> idle -> A -> B)
#
#   Input:  tasks = ["A","A","A","B","B","B"], n = 0
#   Output: 6
# ============================================================

def least_interval(tasks, n):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert least_interval(["A","A","A","B","B","B"], 2) == 8
assert least_interval(["A","C","A","B","D","B"], 1) == 6
assert least_interval(["A","A","A","B","B","B"], 0) == 6
print("All test cases passed!")
