# ============================================================
# PROBLEM: Coin Change
# LeetCode: 322 | https://leetcode.com/problems/coin-change/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given an integer array coins and an integer amount, return
# the fewest number of coins needed to make up that amount.
# If not possible, return -1. You have infinite supply of each coin.
#
# Constraints:
#   - 1 <= len(coins) <= 12
#   - 1 <= coins[i] <= 2^31 - 1
#   - 0 <= amount <= 10^4
#
# Examples:
#   Input:  coins = [1, 5, 10], amount = 12
#   Output: 3 (10 + 1 + 1)
#
#   Input:  coins = [2], amount = 3
#   Output: -1
# ============================================================

def coin_change(coins, amount):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert coin_change([1, 5, 10, 25], 30) == 2
assert coin_change([1, 2, 5], 11) == 3
assert coin_change([2], 3) == -1
assert coin_change([1], 0) == 0
print("All test cases passed!")
