# ============================================================
# PROBLEM: Lowest Common Ancestor of a BST
# LeetCode: 235 | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given a binary search tree (BST), find the lowest common
# ancestor (LCA) of two given nodes p and q.
# The LCA is the lowest node that has both p and q as descendants
# (a node can be a descendant of itself).
#
# Constraints:
#   - The number of nodes is in the range [2, 10^5]
#   - -10^9 <= Node.val <= 10^9
#   - All Node.val are unique
#   - p != q and both exist in the BST
#
# Examples:
#   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#   Output: 6
#
#   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#   Output: 2
# ============================================================

from tree_template import TreeNode, build_tree


def lowest_common_ancestor(root, p, q):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
p = root.left            # node 2
q = root.right           # node 8
assert lowest_common_ancestor(root, p, q).val == 6

p = root.left            # node 2
q = root.left.right     # node 4
assert lowest_common_ancestor(root, p, q).val == 2

print("All test cases passed!")
