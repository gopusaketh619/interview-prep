# ============================================================
# PROBLEM: Accounts Merge
# LeetCode: 721 | https://leetcode.com/problems/accounts-merge/
# Difficulty: Medium | Time to Solve: 30 min
# ============================================================
# Given a list of accounts where accounts[i][0] is a name and
# the rest are emails, merge accounts that share a common email.
# Return accounts in the format [name, sorted emails...].
#
# Constraints:
#   - 1 <= len(accounts) <= 1000
#   - 2 <= len(accounts[i]) <= 10
#   - 1 <= len(accounts[i][j]) <= 30
#
# Examples:
#   Input:  [["John","john@mail","john_work@mail"],["John","john@mail","john00@mail"]]
#   Output: [["John","john00@mail","john@mail","john_work@mail"]]
# ============================================================

from collections import defaultdict


def accounts_merge(accounts):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]
result = accounts_merge(accounts)
result_sorted = sorted([sorted(a) for a in result])
expected = sorted([sorted(a) for a in [
    ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
]])
assert result_sorted == expected
print("All test cases passed!")
