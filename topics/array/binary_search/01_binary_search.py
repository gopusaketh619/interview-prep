# ============================================================
# PROBLEM: Binary Search
# LeetCode: 704 | https://leetcode.com/problems/binary-search/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Constraints:
#   - 1 <= len(nums) <= 10^4
#   - All integers in nums are unique
#   - nums is sorted in ascending order
#   - -10^4 <= nums[i], target <= 10^4
#
# Examples:
#   Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
#   Output: 4
#
#   Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
#   Output: -1
# ============================================================


def binary_search(nums, target):
    # Pattern: Binary search — halve the search space each step
    # Time: O(log n) | Space: O(1)
    #
    # Approach:
    #   1. Maintain low/high pointers defining the search range.
    #   2. Check the middle element each iteration.
    #   3. If target < mid value → search left half, else → search right half.
    #   4. When low > high, search space is empty → target not found.

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1       # target is in left half
        else:
            low = mid + 1        # target is in right half

    return -1


# --- Test Cases ---
assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
assert binary_search([5], 5) == 0
assert binary_search([5], -5) == -1
assert binary_search([1, 2, 3, 4, 5], 1) == 0
assert binary_search([1, 2, 3, 4, 5], 5) == 4
print("All test cases passed!")
