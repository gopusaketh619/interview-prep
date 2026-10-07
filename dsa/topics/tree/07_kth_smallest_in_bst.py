# ============================================================
# PROBLEM: Kth Smallest Element in a BST
# LeetCode: 230 | https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given the root of a BST and an integer k, return the kth
# smallest value (1-indexed) of all the node values in the tree.
#
# Constraints:
#   - The number of nodes is n, 1 <= k <= n <= 10^4
#   - 0 <= Node.val <= 10^4
#
# Examples:
#   Input:  root = [3, 1, 4, null, 2], k = 1
#   Output: 1
#
#   Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
#   Output: 3
# ============================================================

from tree_template import TreeNode, build_tree


def kth_smallest(root, k):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = build_tree([3, 1, 4, None, 2])
assert kth_smallest(root, 1) == 1
assert kth_smallest(root, 2) == 2
assert kth_smallest(root, 3) == 3

root = build_tree([5, 3, 6, 2, 4, None, None, 1])
assert kth_smallest(root, 3) == 3

print("All test cases passed!")
