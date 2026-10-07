# ============================================================
# PROBLEM: Subtree of Another Tree
# LeetCode: 572 | https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given the roots of two binary trees root and subRoot, return
# true if there is a subtree of root with the same structure
# and node values of subRoot.
#
# Constraints:
#   - Number of nodes in root is in the range [1, 2000]
#   - Number of nodes in subRoot is in the range [1, 1000]
#   - -10^4 <= root.val, subRoot.val <= 10^4
#
# Examples:
#   Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
#   Output: True
#
#   Input:  root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#   Output: False
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


def is_subtree(root, sub_root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub = TreeNode(4, TreeNode(1), TreeNode(2))
assert is_subtree(root, sub) == True
print("All test cases passed!")
