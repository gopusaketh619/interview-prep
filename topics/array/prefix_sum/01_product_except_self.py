# ============================================================
# PROBLEM: Product of Array Except Self
# LeetCode: 238 | https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums 
# except nums[i].
#
# You must solve it WITHOUT using division and in O(n) time.
#
# Constraints:
#   - 2 <= len(nums) <= 10^5
#   - -30 <= nums[i] <= 30
#   - The product of any prefix/suffix fits in a 32-bit int
#
# Examples:
#   Input:  nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
#
#   Input:  nums = [-1, 1, 0, -3, 3]
#   Output: [0, 0, 9, 0, 0]
#
# Hint: Use prefix product from left and suffix product from right.
# ============================================================


def product_except_self_brute(nums):
    # Pattern: Brute force — for each index, multiply all other elements
    # Time: O(n^2) | Space: O(1) excluding output
    #
    # Approach:
    #   1. For each index i, loop through all elements except i
    #   2. Multiply them together to get result[i]

    result = []
    for i in range(len(nums)):
        prd = 1
        for j in range(len(nums)):
            if i != j:
                prd = prd * nums[j]
        result.append(prd)
    return result


def product_except_self(nums):
    # Pattern: Prefix/suffix product — two-pass with running multiplier
    # Time: O(n) | Space: O(1) excluding output
    #
    # Approach:
    #   1. Pass 1 (left → right): result[i] = product of everything LEFT of i
    #   2. Pass 2 (right → left): multiply result[i] by product of everything RIGHT of i
    #
    # Key insight: result[i] = prefix_product[0..i-1] × suffix_product[i+1..n-1]
    # By using a running variable for the suffix pass, we avoid a second array.

    nl = len(nums)
    result = [1] * nl

    # Pass 1: build prefix products into result
    prefix = 1
    for i in range(nl):
        result[i] = prefix
        prefix *= nums[i]

    # Pass 2: multiply by suffix products (right to left)
    suffix = 1
    for i in range(nl - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# --- Test Cases ---
assert product_except_self_brute([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self_brute([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
assert product_except_self_brute([2, 3]) == [3, 2]
assert product_except_self_brute([1, 1, 1, 1]) == [1, 1, 1, 1]

assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
assert product_except_self([2, 3]) == [3, 2]
assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]
print("All test cases passed!")
