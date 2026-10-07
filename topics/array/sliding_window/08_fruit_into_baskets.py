# ============================================================
# PROBLEM: Fruit Into Baskets
# LeetCode: 904 | https://leetcode.com/problems/fruit-into-baskets/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# You are visiting a farm with a row of fruit trees. Each tree 
# produces one type of fruit, represented by an integer.
# You have TWO baskets, and each basket can hold only ONE type 
# of fruit (unlimited quantity of that type).
#
# Starting from any tree, you must pick exactly one fruit from 
# every tree moving to the right. You stop when you encounter 
# a third type of fruit (since you only have 2 baskets).
#
# Return the maximum number of fruits you can collect.
#
# (This is equivalent to: find the longest subarray with at 
# most 2 distinct values.)
#
# Constraints:
#   - 1 <= len(fruits) <= 10^5
#   - 0 <= fruits[i] < len(fruits)
#
# Examples:
#   Input:  fruits = [1, 2, 1]
#   Output: 3
#   Explanation: Pick all three → types {1, 2}
#
#   Input:  fruits = [0, 1, 2, 2]
#   Output: 3
#   Explanation: Pick [1, 2, 2] → types {1, 2}
#
#   Input:  fruits = [1, 2, 3, 2, 2]
#   Output: 4
#   Explanation: Pick [2, 3, 2, 2] → types {2, 3}
#
#   Input:  fruits = [3, 1, 3, 1, 2, 1, 1, 2, 3, 3, 4]
#   Output: 5
#   Explanation: Pick [1, 2, 1, 1, 2] → types {1, 2}
# ============================================================


def total_fruit(fruits):
    # Pattern: Variable-size sliding window + frequency hashmap
    # Time: O(n) — each element added/removed at most once
    # Space: O(1) — hashmap holds at most 3 keys before shrinking
    #
    # This is exactly problem #6 (longest subarray with at most k distinct)
    # with k = 2. "2 baskets, each holds one type" = at most 2 distinct values.
    #
    # Approach:
    #   1. Expand window by adding fruits[right] to frequency map.
    #   2. Shrink from left while window has more than 2 distinct fruit types.
    #   3. Update max with current valid window size.

    no_of_trees = len(fruits)
    left = 0
    max_number_of_fruits = 0
    trees_map = {}   # fruit_type → count in current window

    for right in range(no_of_trees):
        # Expand: add right fruit to frequency map
        trees_map[fruits[right]] = trees_map.get(fruits[right], 0) + 1
        # Shrink: while more than 2 fruit types, remove from left
        while len(trees_map) > 2:
            trees_map[fruits[left]] -= 1
            if trees_map[fruits[left]] == 0:
                trees_map.pop(fruits[left])
            left += 1
        # Update: window [left..right] has at most 2 types → valid
        max_number_of_fruits = max(max_number_of_fruits, right - left + 1)

    return max_number_of_fruits



# --- Test Cases ---
assert total_fruit([1, 2, 1]) == 3
assert total_fruit([0, 1, 2, 2]) == 3
assert total_fruit([1, 2, 3, 2, 2]) == 4
assert total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
assert total_fruit([1]) == 1
print("All test cases passed!")
