# ============================================================
# PROBLEM: Daily Temperatures
# LeetCode: 739 | https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array of integers temperatures representing daily
# temperatures, return an array answer such that answer[i] is
# the number of days you have to wait after the ith day to get
# a warmer temperature. If no future day is warmer, answer[i] = 0.
#
# Constraints:
#   - 1 <= len(temperatures) <= 10^5
#   - 30 <= temperatures[i] <= 100
#
# Examples:
#   Input:  temperatures = [73,74,75,71,69,72,76,73]
#   Output: [1,1,4,2,1,1,0,0]
#
#   Input:  temperatures = [30,40,50,60]
#   Output: [1,1,1,0]
# ============================================================

def daily_temperatures(temperatures):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
assert daily_temperatures([30,40,50,60]) == [1,1,1,0]
assert daily_temperatures([30,60,90]) == [1,1,0]
print("All test cases passed!")
