# ============================================================
# PROBLEM: Invert Binary Tree
# LeetCode: 226 | https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given the root of a binary tree, invert the tree (mirror it),
# and return its root.
#
# Constraints:
#   - The number of nodes is in the range [0, 100]
#   - -100 <= Node.val <= 100
#
# Examples:
#   Input:  root = [4, 2, 7, 1, 3, 6, 9]
#   Output: [4, 7, 2, 9, 6, 3, 1]
#
#   Input:  root = [2, 1, 3]
#   Output: [2, 3, 1]
# ============================================================

from tree_template import TreeNode, build_tree


def invert_tree(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def tree_to_list(root):
    """Helper: level-order to list for verification."""
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


# --- Test Cases ---
root = build_tree([4, 2, 7, 1, 3, 6, 9])
inverted = invert_tree(root)
assert tree_to_list(inverted) == [4, 7, 2, 9, 6, 3, 1]

root = build_tree([2, 1, 3])
inverted = invert_tree(root)
assert tree_to_list(inverted) == [2, 3, 1]

assert invert_tree(None) is None
print("All test cases passed!")
