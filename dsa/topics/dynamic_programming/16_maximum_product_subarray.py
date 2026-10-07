# ============================================================
# PROBLEM: Maximum Product Subarray
# LeetCode: 152 | https://leetcode.com/problems/maximum-product-subarray/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given an integer array nums, find a subarray that has the 
# largest product, and return the product.
#
# Constraints:
#   - 1 <= len(nums) <= 2 * 10^4
#   - -10 <= nums[i] <= 10
#   - The product of any prefix/suffix fits in a 32-bit int
#
# Examples:
#   Input:  nums = [2, 3, -2, 4]
#   Output: 6
#   Explanation: [2, 3] has the largest product = 6
#
#   Input:  nums = [-2, 0, -1]
#   Output: 0
#   Explanation: Cannot multiply -2 and -1 without including 0
#
#   Input:  nums = [-2, 3, -4]
#   Output: 24
#   Explanation: [-2, 3, -4] = 24
#
# Hint: Track both max_product and min_product at each step.
#       A negative min can become max when multiplied by negative.
# ============================================================


def max_product(nums):
    # Pattern: Modified Kadane's — track both max and min products
    # Time: O(n) | Space: O(1)
    #
    # Approach:
    #   1. At each element, choose: extend max, extend min, or start fresh.
    #   2. Track cur_min because a large negative × negative = large positive.
    #   3. Update best with the largest product seen so far.
    #
    # Key insight: Unlike max subarray (sums), negatives can flip sign,
    # so today's cur_min can become tomorrow's cur_max.

    cur_max = cur_min = best = nums[0]

    for n in nums[1:]:
        # Must save cur_max before overwriting — both updates need the OLD values
        tmp = cur_max
        cur_max = max(n, tmp * n, cur_min * n)
        cur_min = min(n, tmp * n, cur_min * n)
        best = max(cur_max, best)

    return best


# --- Test Cases ---
assert max_product([2, 3, -2, 4]) == 6
assert max_product([-2, 0, -1]) == 0
assert max_product([-2, 3, -4]) == 24
assert max_product([-2]) == -2
assert max_product([0, 2]) == 2
print("All test cases passed!")
