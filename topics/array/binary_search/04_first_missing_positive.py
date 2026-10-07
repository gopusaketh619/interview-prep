# ============================================================
# PROBLEM: First Missing Positive (Hard)
# LeetCode: 41 | https://leetcode.com/problems/first-missing-positive/
# Difficulty: Hard | Time to Solve: 30 min
# ============================================================
# Given an unsorted integer array nums, return the smallest 
# missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and 
# uses O(1) auxiliary space.
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - -2^31 <= nums[i] <= 2^31 - 1
#
# Examples:
#   Input:  nums = [1, 2, 0]
#   Output: 3
#
#   Input:  nums = [3, 4, -1, 1]
#   Output: 2
#
#   Input:  nums = [7, 8, 9, 11, 12]
#   Output: 1
#
# Hint: Use the array itself as a hash table!
#       Place each number n at index n-1 (if 1 <= n <= len(nums)).
#       Then scan for the first index where nums[i] != i+1.
# ============================================================


def first_missing_positive(nums):
    # Pattern: Cyclic sort — use the array itself as a hash table
    # Time: O(n) | Space: O(1)
    #
    # Approach:
    #   1. Place each value n at index n-1 (swap until correct or out of range).
    #   2. Scan for the first index where nums[i] != i+1 → that's the answer.
    #   3. If all positions match, answer is n+1.
    #
    # Key insight: The answer must be in [1, n+1]. Values outside [1, n]
    # are irrelevant. Each element is swapped at most once → O(n) total.

    n = len(nums)

    for i in range(n):

        while 1 <= nums[i] <= n and nums[i] != i+1:
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]


    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1


# --- Test Cases ---
assert first_missing_positive([1, 2, 0]) == 3
assert first_missing_positive([3, 4, -1, 1]) == 2
assert first_missing_positive([7, 8, 9, 11, 12]) == 1
assert first_missing_positive([1]) == 2
assert first_missing_positive([1, 2, 3]) == 4
print("All test cases passed!")
