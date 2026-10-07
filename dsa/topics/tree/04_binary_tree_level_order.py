# ============================================================
# PROBLEM: Binary Tree Level Order Traversal
# LeetCode: 102 | https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given the root of a binary tree, return the level order
# traversal of its nodes' values (i.e., from left to right,
# level by level).
#
# Constraints:
#   - The number of nodes is in the range [0, 2000]
#   - -1000 <= Node.val <= 1000
#
# Examples:
#   Input:  root = [3, 9, 20, null, null, 15, 7]
#   Output: [[3], [9, 20], [15, 7]]
#
#   Input:  root = [1]
#   Output: [[1]]
# ============================================================

from tree_template import TreeNode, build_tree
from collections import deque


def level_order(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = build_tree([3, 9, 20, None, None, 15, 7])
assert level_order(root) == [[3], [9, 20], [15, 7]]

root = build_tree([1])
assert level_order(root) == [[1]]

assert level_order(None) == []
print("All test cases passed!")
