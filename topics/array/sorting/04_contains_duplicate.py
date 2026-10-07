# ============================================================
# PROBLEM: Contains Duplicate
# LeetCode: 217 | https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element 
# is distinct.
#
# Constraints:
#   - 1 <= len(nums) <= 10^5
#   - -10^9 <= nums[i] <= 10^9
#
# Examples:
#   Input:  nums = [1, 2, 3, 1]
#   Output: True
#
#   Input:  nums = [1, 2, 3, 4]
#   Output: False
#
#   Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
#   Output: True
#
# Think about multiple approaches:
#   - Brute force: O(n^2)
#   - Sorting: O(n log n)
#   - Hash set: O(n)
# ============================================================


def contains_duplicate_brute(nums):
    # Pattern: Brute force — check all pairs
    # Time: O(n^2) | Space: O(1)
    #
    # Approach:
    #   1. For each element, compare it with every element after it
    #   2. If any match, return True

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate(nums):
    # Pattern: Hash set — O(1) existence check
    # Time: O(n) | Space: O(n)
    #
    # Approach:
    #   1. Iterate through nums, checking if each element was already seen.
    #   2. If seen → duplicate found, return True.
    #   3. Otherwise add it to the set for future lookups.
    #
    # Note: use `n in seen` (not `n in hm.keys()`), which is O(1).
    #       `in hm.keys()` creates a view object each time — same result
    #       but `in hm` is cleaner and idiomatic.

    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


def contains_duplicate_sort(nums):
    # Pattern: Sort then check adjacent — duplicates become neighbors
    # Time: O(n log n) | Space: O(1) if in-place sort allowed
    #
    # Approach:
    #   1. Sort the array so duplicates sit next to each other
    #   2. Single pass comparing each element with its predecessor
    #
    # Trade-off: No extra space (unlike hash set) but modifies input
    # and slower than O(n). Good when space is constrained.

    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False


# --- Test Cases ---
assert contains_duplicate_brute([1, 2, 3, 1]) == True
assert contains_duplicate_brute([1, 2, 3, 4]) == False
assert contains_duplicate_brute([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
assert contains_duplicate_brute([1]) == False

assert contains_duplicate([1, 2, 3, 1]) == True
assert contains_duplicate([1, 2, 3, 4]) == False
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
assert contains_duplicate([1]) == False
print("All test cases passed!")
