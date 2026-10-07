# ============================================================
# PROBLEM: Subarrays with K Different Integers (Hard)
# LeetCode: 992 | https://leetcode.com/problems/subarrays-with-k-different-integers/
# Difficulty: Hard | Time to Solve: 35 min
# ============================================================
# Given an integer array nums and an integer k, return the 
# number of contiguous subarrays that contain EXACTLY k 
# distinct integers.
#
# Hint: exact(k) = atMost(k) - atMost(k-1)
# Try writing a helper that counts subarrays with at most k 
# distinct values, then use the formula above.
#
# Constraints:
#   - 1 <= len(nums) <= 2 * 10^4
#   - 1 <= nums[i], k <= len(nums)
#
# Examples:
#   Input:  nums = [1, 2, 1, 2, 3], k = 2
#   Output: 7
#   Explanation: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
#
#   Input:  nums = [1, 2, 1, 3, 4], k = 3
#   Output: 3
#   Explanation: [1,2,1,3], [2,1,3], [1,3,4]
#
#   Input:  nums = [1, 1, 1, 1], k = 1
#   Output: 10
# ============================================================


def at_most_k(nums, k):
    # Helper: count subarrays with AT MOST k distinct integers
    # Pattern: Variable-size sliding window + frequency hashmap
    # Time: O(n) | Space: O(k)
    #
    # Key insight: for each right, the number of valid subarrays
    # ending at right is (right - left + 1). These are:
    #   [left..right], [left+1..right], ..., [right..right]
    # All of them have at most k distinct (since the full window does).

    left = 0
    hm = {}
    result = 0
    for right in range(len(nums)):
        # Expand: add right element to frequency map
        hm[nums[right]] = hm.get(nums[right], 0) + 1
        # Shrink: while more than k distinct, remove from left
        while len(hm) > k:
            hm[nums[left]] -= 1
            if hm[nums[left]] == 0:
                del hm[nums[left]]
            left += 1
        # Count: all subarrays ending at right with at most k distinct
        result += right - left + 1
    return result


def subarrays_with_k_distinct(nums, k):
    # Pattern: exact(k) = atMost(k) - atMost(k-1)
    # Time: O(n) — two passes of O(n) each
    # Space: O(k)
    #
    # Why this works:
    #   atMost(k)   = subarrays with 1 or 2 or ... or k distinct
    #   atMost(k-1) = subarrays with 1 or 2 or ... or (k-1) distinct
    #   Subtracting removes all subarrays with fewer than k distinct,
    #   leaving only those with EXACTLY k distinct.
    #
    # Direct "exactly k" counting is hard because both expanding and
    # shrinking can make the window invalid. The subtraction trick
    # converts it into two "at most" problems, which are standard
    # sliding window.

    return at_most_k(nums, k) - at_most_k(nums, k - 1)


# --- Test Cases ---
assert subarrays_with_k_distinct([1, 2, 1, 2, 3], 2) == 7
assert subarrays_with_k_distinct([1, 2, 1, 3, 4], 3) == 3
assert subarrays_with_k_distinct([1, 1, 1, 1], 1) == 10
assert subarrays_with_k_distinct([1, 2, 3], 3) == 1
print("All test cases passed!")
