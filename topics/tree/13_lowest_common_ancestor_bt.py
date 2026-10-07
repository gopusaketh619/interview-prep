# ============================================================
# PROBLEM: Lowest Common Ancestor of a Binary Tree
# LeetCode: 236 | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given a binary tree, find the lowest common ancestor (LCA)
# of two given nodes p and q. The LCA is the lowest node that
# has both p and q as descendants (a node can be a descendant
# of itself).
#
# Constraints:
#   - The number of nodes is in the range [2, 10^5]
#   - -10^9 <= Node.val <= 10^9
#   - All Node.val are unique
#   - p != q and both exist in the tree
#
# Examples:
#   Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#   Output: 3
#
#   Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#   Output: 5
# ============================================================

class TreeNode:
    # Pattern: <pattern>
    # Time: O(?) per operation | Space: O(?)
    #
    # Approach:
    #   1. <step>

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
# Build tree: 3 -> (5, 1), 5 -> (6, 2), 1 -> (0, 8)
n6 = TreeNode(6)
n2 = TreeNode(2)
n0 = TreeNode(0)
n8 = TreeNode(8)
n5 = TreeNode(5, n6, n2)
n1 = TreeNode(1, n0, n8)
root = TreeNode(3, n5, n1)
assert lowest_common_ancestor(root, n5, n1) == root
print("All test cases passed!")
