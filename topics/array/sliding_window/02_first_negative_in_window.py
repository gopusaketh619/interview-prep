# ============================================================
# PROBLEM: First Negative Number in Every Window of Size K
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given an array of integers and a positive integer k, find 
# the first negative number in every contiguous window of 
# size k. If a window has no negative number, use 0 for that 
# window.
#
# Constraints:
#   - 1 <= k <= len(arr) <= 10^5
#   - -10^5 <= arr[i] <= 10^5
#
# Examples:
#   Input:  arr = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
#   Output: [-1, -1, -7, -15, -15, 0]
#
#   Input:  arr = [-8, 2, 3, -6, 10], k = 2
#   Output: [-8, 0, -6, -6]
#
#   Input:  arr = [1, 2, 3, 4, 5], k = 3
#   Output: [0, 0, 0]
# ============================================================


def first_negative_in_window(arr, k):
    # Brute Force
    # Time: O(n*k) | Space: O(1) excluding output
    #
    # For each window starting at i, scan left-to-right for the
    # first negative. If none found by end of window, append 0.

    result = []
    for i in range(len(arr)-k+1):
        for j in range(i, i+k):
            if arr[j] < 0:
                result.append(arr[j])
                break
            if j-i == k-1:
                result.append(0)
    return result


from collections import deque

def first_negative_optimal(arr, k):
    # Pattern: Fixed-size sliding window + auxiliary deque
    # Time: O(n) | Space: O(k) for the deque
    #
    # Approach:
    #   1. Maintain a deque of indices of negative numbers within
    #      the current window.
    #   2. As the window slides, add new negative indices to the back.
    #   3. Remove indices from the front that have fallen out of the window.
    #   4. The front of the deque is always the first negative in
    #      the current window. If deque is empty, answer is 0.

    dq = deque()       # stores indices of negative elements
    result = []
    l = len(arr)

    for right in range(l):
        # Track: if current element is negative, record its index
        if arr[right] < 0:
            dq.append(right)

        # Window is fully formed once right >= k-1
        if right >= k-1:
            # Shrink: discard indices that are outside the window's left boundary
            while dq and dq[0] < right - k + 1:
                dq.popleft()
            # Answer: front of deque is the first negative, else 0
            result.append(arr[dq[0]] if dq else 0)
    return result


# --- Test Cases ---
assert first_negative_in_window([12, -1, -7, 8, -15, 30, 16, 28], 3) == [-1, -1, -7, -15, -15, 0]
assert first_negative_in_window([-8, 2, 3, -6, 10], 2) == [-8, 0, -6, -6]
assert first_negative_in_window([1, 2, 3, 4, 5], 3) == [0, 0, 0]

assert first_negative_optimal([12, -1, -7, 8, -15, 30, 16, 28], 3) == [-1, -1, -7, -15, -15, 0]
assert first_negative_optimal([-8, 2, 3, -6, 10], 2) == [-8, 0, -6, -6]
assert first_negative_optimal([1, 2, 3, 4, 5], 3) == [0, 0, 0]
print("All test cases passed!")
