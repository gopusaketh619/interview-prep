# ============================================================
# DYNAMIC PROGRAMMING - PATTERN TEMPLATE
# ============================================================
#
# DP solves problems with overlapping subproblems and optimal
# substructure by storing results to avoid recomputation.
#
# APPROACH:
#   1. Define state: what does dp[i] (or dp[i][j]) represent?
#   2. Find recurrence: how does dp[i] relate to prior states?
#   3. Set base case(s).
#   4. Determine traversal order (ensure dependencies computed first).
#   5. Return answer (often dp[n] or dp[n-1]).
#
# COMMON PATTERNS:
#
#   1. Linear (1D):
#      dp[i] = f(dp[i-1], dp[i-2], ...)
#      Examples: Climbing Stairs, House Robber, Coin Change
#
#   2. Two-sequence (2D):
#      dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
#      Examples: LCS, Edit Distance, Unique Paths
#
#   3. Knapsack:
#      dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
#      Examples: 0/1 Knapsack, Partition Equal Subset Sum
#
#   4. Interval:
#      dp[i][j] = optimal over all splits k in [i, j]
#      Examples: Matrix Chain, Burst Balloons
#
#   5. String:
#      dp[i][j] = property of s[i:j] or alignment of s1[:i], s2[:j]
#      Examples: Longest Palindromic Substring, Word Break
#
# SIGNALS IT'S A DP PROBLEM:
#   - "Count the number of ways..."
#   - "What is the minimum/maximum..."
#   - "Is it possible to..."
#   - "Longest/shortest..."
#   - Choices at each step, can't use greedy
#
# TOP-DOWN (Memoization):
#   @lru_cache(maxsize=None)
#   def solve(state):
#       if base_case: return ...
#       return recurrence(solve(sub_state))
#
# BOTTOM-UP (Tabulation):
#   dp = [base] * (n + 1)
#   for i in range(1, n + 1):
#       dp[i] = recurrence(dp[...])
#   return dp[n]
#
# SPACE OPTIMIZATION:
#   If dp[i] only depends on dp[i-1] (or dp[i-1] and dp[i-2]),
#   you can reduce space from O(n) to O(1).
#
# TIME: Varies (states * transition cost)
# SPACE: O(states) or O(1) if optimized
# ============================================================
