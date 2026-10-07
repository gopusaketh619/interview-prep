# ============================================================
# PROBLEM: Maximum Subarray (Kadane's Algorithm)
# LeetCode: 53 | https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an integer array nums, find the subarray with the 
# largest sum, and return its sum.
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - -10^4 <= nums[i] <= 10^4
#
# Examples:
#   Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   Output: 6
#   Explanation: Subarray [4, -1, 2, 1] has the largest sum = 6
#
#   Input:  nums = [1]
#   Output: 1
#
#   Input:  nums = [5, 4, -1, 7, 8]
#   Output: 23
#
#   Input:  nums = [-1]
#   Output: -1
#
# Hint: At each position decide: extend current subarray or
#       start fresh from here. This is Kadane's algorithm.
# ============================================================


def max_subarray(nums):
    # Pattern: Kadane's Algorithm — single pass, extend or restart
    # Time: O(n) | Space: O(1)
    #
    # Approach:
    #   1. At each element, decide: extend the current subarray or start fresh.
    #   2. Extend if current_sum + n > n (i.e., current_sum > 0).
    #      Start fresh if the running sum has gone negative (it would only hurt).
    #   3. Track the best sum seen across all decisions.
    #
    # Key insight: Similar to buy_sell_stock — instead of tracking
    # "min price so far", we track "best sum ending here".

    current = best = nums[0]

    for n in nums[1:]:
        # Extend current subarray or start fresh from n
        current = max(current + n, n)
        # Update global best if this subarray is the largest so far
        best = max(best, current)
    return best


# --- Test Cases ---
assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray([1]) == 1
assert max_subarray([5, 4, -1, 7, 8]) == 23
assert max_subarray([-1]) == -1
assert max_subarray([-2, -1]) == -1
print("All test cases passed!")
