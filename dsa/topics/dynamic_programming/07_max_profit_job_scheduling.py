# ============================================================
# PROBLEM: Maximum Profit in Job Scheduling
# LeetCode: 1235 | https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Difficulty: Hard | Time to Solve: 35 min
# ============================================================
# Given n jobs where each job has startTime, endTime, and profit,
# find the maximum profit you can take such that no two selected
# jobs overlap.
#
# Constraints:
#   - 1 <= len(startTime) == len(endTime) == len(profit) <= 5 * 10^4
#   - 1 <= startTime[i] < endTime[i] <= 10^9
#   - 1 <= profit[i] <= 10^4
#
# Examples:
#   Input:  startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
#   Output: 120 (jobs 1 and 4: 50 + 70)
# ============================================================

def job_scheduling(start_time, end_time, profit):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert job_scheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]) == 120
assert job_scheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]) == 150
assert job_scheduling([1,1,1], [2,3,4], [5,6,4]) == 6
print("All test cases passed!")
