# ============================================================
# PROBLEM: Best Time to Buy and Sell Stock
# LeetCode: 121 | https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given an array prices where prices[i] is the price of a stock 
# on the ith day, find the maximum profit you can achieve.
#
# You must buy before you sell (buy on day i, sell on day j 
# where i < j). If no profit is possible, return 0.
#
# Constraints:
#   - 1 <= len(prices) <= 10^5
#   - 0 <= prices[i] <= 10^4
#
# Examples:
#   Input:  prices = [7, 1, 5, 3, 6, 4]
#   Output: 5
#   Explanation: Buy on day 2 (price=1), sell on day 5 (price=6)
#
#   Input:  prices = [7, 6, 4, 3, 1]
#   Output: 0
#   Explanation: Prices only decrease, no profit possible
#
#   Input:  prices = [2, 4, 1]
#   Output: 2
#
# Hint: Track the minimum price seen so far. At each day,
#       compute profit = current price - min_price_so_far.
# ============================================================


def max_profit_brute(prices):
    # Pattern: Brute force — check all buy/sell pairs
    # Time: O(n^2) | Space: O(1)
    #
    # Approach:
    #   1. Try every pair (buy day, sell day) where buy < sell
    #   2. Track the maximum profit seen across all pairs

    max_profit = 0
    for buy in range(len(prices)-1):
        for sell in range(buy+1, len(prices)):
            max_profit = max(max_profit, prices[sell] - prices[buy])
    return max_profit


def max_profit(prices):
    # Pattern: Single pass — track min price so far
    # Time: O(n) | Space: O(1)
    #
    # Approach:
    #   1. Track the minimum price seen so far (best buy day).
    #   2. At each day, compute profit if we sold today.
    #   3. Update max_profit if this profit is the best so far.
    #
    # Key insight: The best profit ending at day i always uses
    # the lowest price from days 0..i-1 as the buy price.

    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        today_price = prices[i]
        # What profit would we get selling today?
        profit = today_price - min_price
        max_profit = max(max_profit, profit)
        # Would today be a better buy day for future sells?
        min_price = min(today_price, min_price)
    return max_profit
        


# --- Test Cases ---
assert max_profit_brute([7, 1, 5, 3, 6, 4]) == 5
assert max_profit_brute([7, 6, 4, 3, 1]) == 0
assert max_profit_brute([2, 4, 1]) == 2
assert max_profit_brute([1]) == 0
assert max_profit_brute([1, 2]) == 1

assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
assert max_profit([2, 4, 1]) == 2
assert max_profit([1]) == 0
assert max_profit([1, 2]) == 1
print("All test cases passed!")
