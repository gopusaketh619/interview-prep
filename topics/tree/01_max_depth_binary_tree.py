# ============================================================
# PROBLEM: Maximum Depth of Binary Tree
# LeetCode: 104 | https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along
# the longest path from the root node down to the farthest leaf.
#
# Constraints:
#   - The number of nodes is in the range [0, 10^4]
#   - -100 <= Node.val <= 100
#
# Examples:
#   Input:  root = [3, 9, 20, null, null, 15, 7]
#   Output: 3
#
#   Input:  root = [1, null, 2]
#   Output: 2
# ============================================================

from tree_template import TreeNode, build_tree
from collections import deque


def max_depth_recursive(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def max_depth_iterative(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = build_tree([3, 9, 20, None, None, 15, 7])
assert max_depth_recursive(root) == 3
assert max_depth_iterative(root) == 3

root = build_tree([1, None, 2])
assert max_depth_recursive(root) == 2

assert max_depth_recursive(None) == 0
print("All test cases passed!")
