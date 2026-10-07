# ============================================================
# PROBLEM: Binary Tree Right Side View
# LeetCode: 199 | https://leetcode.com/problems/binary-tree-right-side-view/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given the root of a binary tree, imagine yourself standing
# on the right side of it. Return the values of the nodes you
# can see ordered from top to bottom.
#
# Constraints:
#   - The number of nodes is in the range [0, 100]
#   - -100 <= Node.val <= 100
#
# Examples:
#   Input:  root = [1, 2, 3, null, 5, null, 4]
#   Output: [1, 3, 4]
#
#   Input:  root = [1, null, 3]
#   Output: [1, 3]
# ============================================================

from tree_template import TreeNode, build_tree
from collections import deque


def right_side_view(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = build_tree([1, 2, 3, None, 5, None, 4])
assert right_side_view(root) == [1, 3, 4]

root = build_tree([1, None, 3])
assert right_side_view(root) == [1, 3]

assert right_side_view(None) == []
print("All test cases passed!")
