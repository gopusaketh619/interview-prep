# ============================================================
# PROBLEM: 3Sum
# LeetCode: 15 | https://leetcode.com/problems/3sum/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, 
# j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# The solution set must not contain duplicate triplets.
#
# Constraints:
#   - 3 <= len(nums) <= 3000
#   - -10^5 <= nums[i] <= 10^5
#
# Examples:
#   Input:  nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1, -1, 2], [-1, 0, 1]]
#
#   Input:  nums = [0, 1, 1]
#   Output: []
#
#   Input:  nums = [0, 0, 0]
#   Output: [[0, 0, 0]]
# ============================================================




def three_sum_brute(nums):
    # Pattern: Brute force — check all triplets, deduplicate with set
    # Time: O(n^3) | Space: O(n)
    #
    # Approach:
    #   1. Try every combination of three distinct indices
    #   2. Sort each triplet and store in a set to avoid duplicates

    triplets = set()
    ln = len(nums)
    for i in range(0, ln-2):
        for j in range(i+1, ln-1):
            for k in range(j+1, ln):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return [list(t) for t in triplets]


def three_sum(nums):
    # Pattern: Sort + fix one element + two pointers for the other two
    # Time: O(n^2) | Space: O(1) excluding output
    #
    # Approach:
    #   1. Sort the array (enables two pointers + easy duplicate skipping).
    #   2. Fix element i, then use two pointers (left, right) to find
    #      pairs that sum to -nums[i].
    #   3. Skip duplicate values of i, left, right to avoid duplicate triplets.
    #
    # Key insight: Reduces 3Sum to multiple Two Sum problems.
    # Sorting groups duplicates together so we can skip them with a simple check.

    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate i values (already processed this number)
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicate left values
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate right values
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # Move both pointers inward past the last duplicates
                left += 1
                right -= 1

    return result
            




# --- Test Cases ---
result = three_sum([-1, 0, 1, 2, -1, -4])
assert sorted([sorted(x) for x in result]) == sorted([[-1, -1, 2], [-1, 0, 1]])
assert three_sum([0, 1, 1]) == []
assert three_sum([0, 0, 0]) == [[0, 0, 0]]
assert three_sum([1, -1, -1, 0]) == [[-1, 0, 1]]
print("All test cases passed!")
