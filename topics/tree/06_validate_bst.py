# ============================================================
# PROBLEM: Validate Binary Search Tree
# LeetCode: 98 | https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given the root of a binary tree, determine if it is a
# valid binary search tree (BST).
#
# Constraints:
#   - The number of nodes is in the range [1, 10^4]
#   - -2^31 <= Node.val <= 2^31 - 1
#
# Examples:
#   Input:  root = [2, 1, 3]
#   Output: True
#
#   Input:  root = [5, 1, 4, null, null, 3, 6]
#   Output: False (4 < 5 but is right child)
# ============================================================

from tree_template import TreeNode, build_tree


def is_valid_bst(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def is_valid_bst_inorder(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = build_tree([2, 1, 3])
assert is_valid_bst(root) == True
assert is_valid_bst_inorder(root) == True

root = build_tree([5, 1, 4, None, None, 3, 6])
assert is_valid_bst(root) == False
assert is_valid_bst_inorder(root) == False

root = build_tree([5, 4, 6, None, None, 3, 7])
assert is_valid_bst(root) == False

print("All test cases passed!")
