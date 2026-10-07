# ============================================================
# PROBLEM: Remove Duplicates from Sorted Array
# LeetCode: 26 | https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given a sorted array nums, remove the duplicates in-place 
# such that each unique element appears only once. Return the 
# number of unique elements.
#
# The first k elements of nums should hold the unique elements 
# in their original order. It doesn't matter what you leave 
# beyond the first k elements.
#
# Constraints:
#   - 1 <= len(nums) <= 3 * 10^4
#   - -100 <= nums[i] <= 100
#   - nums is sorted in non-decreasing order
#
# Examples:
#   Input:  nums = [1, 1, 2]
#   Output: 2, nums = [1, 2, ...]
#
#   Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#   Output: 5, nums = [0, 1, 2, 3, 4, ...]
# ============================================================


def remove_duplicates(nums):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
nums1 = [1, 1, 2]
assert remove_duplicates(nums1) == 2
assert nums1[:2] == [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
assert remove_duplicates(nums2) == 5
assert nums2[:5] == [0, 1, 2, 3, 4]

nums3 = [1]
assert remove_duplicates(nums3) == 1

nums4 = [1, 2, 3]
assert remove_duplicates(nums4) == 3
print("All test cases passed!")
