# ============================================================
# PROBLEM: Max Consecutive Ones III
# LeetCode: 1004 | https://leetcode.com/problems/max-consecutive-ones-iii/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given a binary array nums and an integer k, return the 
# maximum number of consecutive 1's in the array if you can 
# flip at most k 0's.
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - nums[i] is either 0 or 1
#   - 0 <= k <= len(nums)
#
# Examples:
#   Input:  nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#   Output: 6
#   Explanation: Flip the 0's at index 5 and 10 → [1,1,1,0,0,1,1,1,1,1,1]
#               Longest run of 1's = 6 (index 5 to 10)
#
#   Input:  nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
#   Output: 10
#   Explanation: Flip 0's at index 4, 5, 9 → longest run = 10
#
#   Input:  nums = [1,1,1,1], k = 0
#   Output: 4
# ============================================================


def longest_ones(nums, k):
    # Pattern: Variable-size sliding window + zero counter
    # Time: O(n) — each element visited at most twice (once by right, once by left)
    # Space: O(1) — only a counter and two pointers
    #
    # Approach:
    #   1. Expand window by moving right. Count zeros in the window.
    #   2. Shrink from left while zeros in window exceed k (our flip budget).
    #   3. Update max_len — the window always contains at most k zeros,
    #      meaning we can flip them all to get a valid run of 1's.
    #
    # Key insight: "flip at most k zeros" is the same as
    # "find longest window with at most k zeros".

    number_of_zeros = 0
    max_len = 0
    left = 0

    for right in range(len(nums)):
        # Expand: if new element is 0, increment zero count
        if nums[right] == 0:
            number_of_zeros += 1
        # Shrink: while we've used more than k flips, move left
        while number_of_zeros > k:
            if nums[left] == 0:
                number_of_zeros -= 1
            left += 1
        # Update: window [left..right] has at most k zeros → valid
        max_len = max(max_len, right - left + 1)
    
    return max_len



# --- Test Cases ---
assert longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
assert longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
assert longest_ones([1,1,1,1], 0) == 4
assert longest_ones([0,0,0], 0) == 0
assert longest_ones([0,0,0], 3) == 3
print("All test cases passed!")
