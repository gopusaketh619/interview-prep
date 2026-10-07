# ============================================================
# TREE - PATTERN TEMPLATE
# ============================================================
#
# A tree is a hierarchical structure with nodes connected by edges.
# Binary tree: each node has at most 2 children (left, right).
#
# NODE DEFINITION:
#   class TreeNode:
#       def __init__(self, val=0, left=None, right=None):
#           self.val = val
#           self.left = left
#           self.right = right
#
# TRAVERSALS:
#
#   1. Inorder (Left → Root → Right) — gives sorted order for BST:
#      def inorder(node):
#          if not node: return
#          inorder(node.left)
#          visit(node)
#          inorder(node.right)
#
#   2. Preorder (Root → Left → Right) — useful for serialization:
#      def preorder(node):
#          if not node: return
#          visit(node)
#          preorder(node.left)
#          preorder(node.right)
#
#   3. Postorder (Left → Right → Root) — useful for deletion:
#      def postorder(node):
#          if not node: return
#          postorder(node.left)
#          postorder(node.right)
#          visit(node)
#
#   4. Level-order (BFS):
#      from collections import deque
#      queue = deque([root])
#      while queue:
#          node = queue.popleft()
#          visit(node)
#          if node.left: queue.append(node.left)
#          if node.right: queue.append(node.right)
#
# KEY TECHNIQUES:
#   - Recursion with base case: if not node: return
#   - DFS for path/sum problems
#   - BFS for level-order problems
#   - BST property: left.val < node.val < right.val
#   - Return multiple values (e.g., height + is_balanced)
#
# BST OPERATIONS:
#   - Search: go left if target < node, right if target > node
#   - Insert: find null spot using BST property
#   - Inorder traversal = sorted output
#
# WHEN TO USE:
#   - Hierarchical data
#   - BST for ordered operations
#   - Tree traversal variations
#   - Subtree matching
#   - Path sum problems
#
# TIME: O(n) for traversal, O(log n) for balanced BST ops
# SPACE: O(h) where h = height (O(log n) balanced, O(n) skewed)
# ============================================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Helper: build tree from level-order list (None for missing nodes)."""
    if not values:
        return None
    from collections import deque
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
