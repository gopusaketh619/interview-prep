# ============================================================
# PROBLEM: Serialize and Deserialize Binary Tree
# LeetCode: 297 | https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Difficulty: Hard | Time to Solve: 35 min
# ============================================================
# Design an algorithm to serialize and deserialize a binary tree.
# Serialization is converting a tree to a string.
# Deserialization is reconstructing the tree from the string.
#
# Constraints:
#   - The number of nodes is in the range [0, 10^4]
#   - -1000 <= Node.val <= 1000
#
# Examples:
#   Input:  root = [1, 2, 3, null, null, 4, 5]
#   Output: [1, 2, 3, null, null, 4, 5] (same tree after serialize/deserialize)
# ============================================================

from tree_template import TreeNode
from collections import deque


class Codec:

    def serialize(self, root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

        pass

    def deserialize(self, data):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

        pass


# --- Test Cases ---
codec = Codec()

from tree_template import build_tree as bt
root = bt([1, 2, 3, None, None, 4, 5])
serialized = codec.serialize(root)
deserialized = codec.deserialize(serialized)
assert codec.serialize(deserialized) == serialized

assert codec.deserialize(codec.serialize(None)) is None

root = bt([1])
assert codec.deserialize(codec.serialize(root)).val == 1

print("All test cases passed!")
