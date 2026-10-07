# ============================================================
# PROBLEM: Balanced Binary Tree
# LeetCode: 110 | https://leetcode.com/problems/balanced-binary-tree/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given a binary tree, determine if it is height-balanced.
# A height-balanced tree: for every node, the depth of the
# two subtrees never differs by more than one.
#
# Constraints:
#   - The number of nodes is in the range [0, 5000]
#   - -10^4 <= Node.val <= 10^4
#
# Examples:
#   Input:  root = [3, 9, 20, null, null, 15, 7]
#   Output: True
#
#   Input:  root = [1, 2, 2, 3, 3, null, null, 4, 4]
#   Output: False
# ============================================================

from tree_template import TreeNode, build_tree


def is_balanced(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = build_tree([3, 9, 20, None, None, 15, 7])
assert is_balanced(root) == True

root = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
assert is_balanced(root) == False

assert is_balanced(None) == True
print("All test cases passed!")
