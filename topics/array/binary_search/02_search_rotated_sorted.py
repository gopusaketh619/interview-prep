# ============================================================
# PROBLEM: Search in Rotated Sorted Array
# LeetCode: 33 | https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# An integer array nums sorted in ascending order (with distinct 
# values) is possibly rotated at an unknown pivot index k.
# For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
#
# Given the rotated array and a target, return the index of 
# target if it is in nums, or -1 if it is not.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Constraints:
#   - 1 <= len(nums) <= 5000
#   - -10^4 <= nums[i], target <= 10^4
#   - All values in nums are unique
#
# Examples:
#   Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
#   Output: 4
#
#   Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
#   Output: -1
#
#   Input:  nums = [1], target = 0
#   Output: -1
#
# Hint: One half is always sorted. Determine which half target
#       belongs to, then search that half.
# ============================================================


def search_rotated(nums, target):
    # Pattern: Modified binary search — determine which half is sorted
    # Time: O(log n) | Space: O(1)
    #
    # Approach:
    #   1. Standard binary search structure (low, high, mid).
    #   2. At each step, one half is always sorted (the rotation
    #      only breaks one half).
    #   3. Check if target falls within the sorted half's range.
    #      If yes → search that half. If no → search the other half.
    #
    # Key insight: In a normal binary search, one comparison tells you
    # which half to search. Here you need two: which half is sorted,
    # then is target in that sorted range.

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            # Left half [low..mid] is sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1       # target is in sorted left half
            else:
                low = mid + 1        # target must be in right half
        else:
            # Right half [mid..high] is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1        # target is in sorted right half
            else:
                high = mid - 1       # target must be in left half

    return -1
        


# --- Test Cases ---
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_rotated([1], 0) == -1
assert search_rotated([1], 1) == 0
assert search_rotated([3, 1], 1) == 1
print("All test cases passed!")
