# ============================================================
# PROBLEM: Two Sum
# LeetCode: 1 | https://leetcode.com/problems/two-sum/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given an array of integers nums and an integer target,
# return indices of the two numbers that add up to target.
# You may assume each input has exactly one solution, and
# you may not use the same element twice.
#
# Constraints:
#   - 2 <= len(nums) <= 10^4
#   - -10^9 <= nums[i] <= 10^9
#   - Exactly one valid answer exists
#
# Examples:
#   Input:  nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
#   Explanation: nums[0] + nums[1] = 2 + 7 = 9
#
#   Input:  nums = [3, 2, 4], target = 6
#   Output: [1, 2]
#
#   Input:  nums = [3, 3], target = 6
#   Output: [0, 1]
# ============================================================


def two_sum_brute(nums, target):
    # Pattern: Brute force — check all pairs
    # Time: O(n^2) | Space: O(1)
    #
    # Approach:
    #   1. For each element at index i, check every element at index j > i
    #   2. If nums[i] + nums[j] == target, return [i, j]

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def two_sum(nums, target):
    # Pattern: Hash map — one-pass complement lookup
    # Time: O(n) | Space: O(n)
    #
    # Approach:
    #   1. For each element, compute its complement (target - nums[i])
    #   2. If complement already exists in the map, we found the pair
    #   3. Otherwise, store nums[i] → i for future lookups
    #
    # Key insight: By storing as we go, when we find a complement
    # in the map, its index is guaranteed to be earlier than i.

    hm = {}  # value → index
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hm:
            return [hm[complement], i]
        hm[nums[i]] = i
    return None



# --- Test Cases ---
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum_brute([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_brute([3, 2, 4], 6) == [1, 2]
assert two_sum_brute([3, 3], 6) == [0, 1]
print("All test cases passed!")
