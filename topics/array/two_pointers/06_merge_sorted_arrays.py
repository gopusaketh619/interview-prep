# ============================================================
# PROBLEM: Merge Sorted Array
# LeetCode: 88 | https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# You are given two integer arrays nums1 and nums2, sorted in 
# non-decreasing order, and two integers m and n, representing 
# the number of elements in nums1 and nums2 respectively.
#
# Merge nums2 into nums1 as one sorted array IN-PLACE.
# nums1 has a length of m + n, where the last n elements are 
# set to 0 and should be ignored.
#
# Constraints:
#   - nums1.length == m + n
#   - nums2.length == n
#   - 0 <= m, n <= 200
#   - -10^9 <= nums1[i], nums2[j] <= 10^9
#
# Examples:
#   Input:  nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
#   Output: [1,2,2,3,5,6]
#
#   Input:  nums1 = [1], m=1, nums2 = [], n=0
#   Output: [1]
#
#   Input:  nums1 = [0], m=0, nums2 = [1], n=1
#   Output: [1]
#
# Hint: Start from the RIGHT (largest elements) to avoid
#       overwriting elements in nums1 that haven't been processed.
# ============================================================


def merge(nums1, m, nums2, n):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
nums1 = [1, 2, 3, 0, 0, 0]
merge(nums1, 3, [2, 5, 6], 3)
assert nums1 == [1, 2, 2, 3, 5, 6]

nums2 = [1]
merge(nums2, 1, [], 0)
assert nums2 == [1]

nums3 = [0]
merge(nums3, 0, [1], 1)
assert nums3 == [1]

nums4 = [4, 5, 6, 0, 0, 0]
merge(nums4, 3, [1, 2, 3], 3)
assert nums4 == [1, 2, 3, 4, 5, 6]
print("All test cases passed!")
