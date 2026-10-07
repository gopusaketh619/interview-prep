# ============================================================
# PROBLEM: Sort Colors (Dutch National Flag)
# LeetCode: 75 | https://leetcode.com/problems/sort-colors/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an array nums with n objects colored red (0), white (1),
# or blue (2), sort them in-place so that objects of the same 
# color are adjacent, in the order red, white, blue.
#
# You must solve this without using the library sort function.
# Can you do it in one pass with O(1) extra space?
#
# Constraints:
#   - 1 <= len(nums) <= 300
#   - nums[i] is 0, 1, or 2
#
# Examples:
#   Input:  nums = [2, 0, 2, 1, 1, 0]
#   Output: [0, 0, 1, 1, 2, 2]
#
#   Input:  nums = [2, 0, 1]
#   Output: [0, 1, 2]
#
#   Input:  nums = [0]
#   Output: [0]
# ============================================================


def sort_colors(nums):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
nums1 = [2, 0, 2, 1, 1, 0]
sort_colors(nums1)
assert nums1 == [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sort_colors(nums2)
assert nums2 == [0, 1, 2]

nums3 = [0]
sort_colors(nums3)
assert nums3 == [0]

nums4 = [1, 2, 0, 1, 2, 0]
sort_colors(nums4)
assert nums4 == [0, 0, 1, 1, 2, 2]
print("All test cases passed!")
