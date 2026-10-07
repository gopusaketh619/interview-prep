# ============================================================
# PROBLEM: Construct Binary Tree from Preorder and Inorder
# LeetCode: 105 | https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given two integer arrays preorder and inorder where preorder
# is the preorder traversal and inorder is the inorder traversal
# of the same tree, construct and return the binary tree.
#
# Constraints:
#   - 1 <= len(preorder) <= 3000
#   - preorder.length == inorder.length
#   - -3000 <= preorder[i], inorder[i] <= 3000
#   - All values are unique
#
# Examples:
#   Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#   Output: [3, 9, 20, null, null, 15, 7]
# ============================================================

from tree_template import TreeNode


def build_tree(preorder, inorder):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def tree_inorder(root):
    """Helper for verification."""
    if not root:
        return []
    return tree_inorder(root.left) + [root.val] + tree_inorder(root.right)


def tree_preorder(root):
    """Helper for verification."""
    if not root:
        return []
    return [root.val] + tree_preorder(root.left) + tree_preorder(root.right)


# --- Test Cases ---
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = build_tree(preorder, inorder)
assert tree_preorder(root) == [3, 9, 20, 15, 7]
assert tree_inorder(root) == [9, 3, 15, 20, 7]

preorder = [-1]
inorder = [-1]
root = build_tree(preorder, inorder)
assert root.val == -1

print("All test cases passed!")
