# ============================================================
# PROBLEM: Sliding Window Maximum (Hard)
# LeetCode: 239 | https://leetcode.com/problems/sliding-window-maximum/
# Difficulty: Hard | Time to Solve: 30 min
# ============================================================
# Given an array of integers nums and a sliding window of 
# size k, return an array of the maximum value in each window 
# as it slides from left to right.
#
# Constraints:
#   - 1 <= k <= len(nums) <= 10^5
#   - -10^4 <= nums[i] <= 10^4
#
# Follow-up: Can you solve it in O(n) time?
# Hint: Think about a monotonic deque.
#
# Examples:
#   Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
#   Output: [3, 3, 5, 5, 6, 7]
#   Explanation:
#     Window [1, 3, -1]     → max = 3
#     Window [3, -1, -3]    → max = 3
#     Window [-1, -3, 5]    → max = 5
#     Window [-3, 5, 3]     → max = 5
#     Window [5, 3, 6]      → max = 6
#     Window [3, 6, 7]      → max = 7
#
#   Input:  nums = [1], k = 1
#   Output: [1]
#
#   Input:  nums = [9, 11], k = 2
#   Output: [11]
# ============================================================


from collections import deque


def max_sliding_window(nums, k):
    # Brute Force
    # Time: O(n*k) | Space: O(1) excluding output
    #
    # For each window position, compute max by scanning all k elements.

    result = []
    for i in range(len(nums)-k+1):
        result.append(max(nums[i:i+k]))
    return result


def max_sliding_window_optimal(nums, k):
    # Pattern: Fixed-size sliding window + monotonic decreasing deque
    # Time: O(n) — each element is pushed/popped at most once
    # Space: O(k) for the deque
    #
    # Approach:
    #   1. Maintain a deque of INDICES whose values are in decreasing order.
    #   2. The front of the deque is always the index of the max in the window.
    #   3. Before adding a new element, pop all smaller elements from the back
    #      (they can never be the max while the new element exists in the window).
    #   4. Remove the front if its index has fallen outside the window.
    #   5. Once window is fully formed (right >= k-1), front = answer.

    dq = deque()   # stores indices; values at those indices are decreasing
    result = []

    for right in range(len(nums)):
        # Maintain monotonic property: remove smaller elements from back
        # (they're useless — a newer, larger element will always beat them)
        while dq and nums[dq[-1]] <= nums[right]:
            dq.pop()
        dq.append(right)

        # Expire: if front index is outside window, discard it.
        # Only one element can expire per step (window shifts by 1).
        if dq[0] < right - k + 1:
            dq.popleft()

        # Window fully formed: front of deque = max of current window
        if right >= k-1:
            result.append(nums[dq[0]])

    return result 





# --- Test Cases ---
assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert max_sliding_window([1], 1) == [1]
assert max_sliding_window([9, 11], 2) == [11]
assert max_sliding_window([4, -2], 2) == [4]
assert max_sliding_window([7, 7, 7, 7], 2) == [7, 7, 7]


assert max_sliding_window_optimal([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert max_sliding_window_optimal([1], 1) == [1]
assert max_sliding_window_optimal([9, 11], 2) == [11]
assert max_sliding_window_optimal([4, -2], 2) == [4]
assert max_sliding_window_optimal([7, 7, 7, 7], 2) == [7, 7, 7]
print("All test cases passed!")
