# ============================================================
# PROBLEM: Maximum Average Subarray of Size K
# LeetCode: 643 | https://leetcode.com/problems/maximum-average-subarray-i/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given an integer array nums and an integer k, find the 
# contiguous subarray of length k that has the maximum average 
# value. Return the maximum average.
#
# Constraints:
#   - 1 <= k <= len(nums) <= 10^5
#   - -10^4 <= nums[i] <= 10^4
#
# Examples:
#   Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
#   Output: 12.75
#   Explanation: Maximum average is (12 + -5 + -6 + 50) / 4 = 12.75
#
#   Input:  nums = [5], k = 1
#   Output: 5.0
# ============================================================


def max_average_subarray(nums, k):
    # Pattern: Fixed-size sliding window
    # Time: O(n) | Space: O(1)
    #
    # Approach:
    #   1. Compute sum of the first window of size k
    #   2. Slide the window one element at a time:
    #      add the incoming element, subtract the outgoing element
    #   3. Track the maximum window sum seen so far
    #   4. Return max_sum / k for the average

    # Initialize: sum of the first window [0..k-1]
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide: right pointer moves from index k to end
    for right in range(k, len(nums)):
        # Expand right, shrink left: the element leaving is nums[right - k]
        window_sum += nums[right] - nums[right - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k
    


# --- Test Cases ---
assert max_average_subarray([1, 12, -5, -6, 50, 3], 4) == 12.75
assert max_average_subarray([5], 1) == 5.0
assert max_average_subarray([0, 4, 0, 3, 2], 1) == 4.0
print("All test cases passed!")
