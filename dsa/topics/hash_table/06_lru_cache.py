# ============================================================
# PROBLEM: LRU Cache
# LeetCode: 146 | https://leetcode.com/problems/lru-cache/
# Difficulty: Medium | Time to Solve: 30 min
# ============================================================
# Design a data structure that follows the constraints of a
# Least Recently Used (LRU) cache.
#   - LRUCache(capacity): Initialize with positive capacity.
#   - get(key): Return value if key exists, otherwise return -1.
#   - put(key, value): Update or insert. Evict LRU key if at capacity.
# Both get and put must run in O(1) average time.
#
# Constraints:
#   - 1 <= capacity <= 3000
#   - 0 <= key <= 10^4
#   - 0 <= value <= 10^5
#   - At most 2 * 10^5 calls to get and put
#
# Examples:
#   Input:  LRUCache(2), put(1,1), put(2,2), get(1) -> 1
#           put(3,3), get(2) -> -1 (evicted)
# ============================================================

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    # Pattern: Doubly linked list + hashmap
    # Time: O(1) per get/put | Space: O(capacity)
    #
    # Approach:
    #   1. Hashmap stores key -> node for O(1) lookup.
    #   2. Doubly linked list tracks usage order
    #      (head.next = LRU, tail.prev = most recent).
    #   3. On get: move node to end (most recently used).
    #   4. On put: add/update node, evict LRU from front if over capacity.
    #
    # Key insight: Dummy head/tail avoid null-check edge cases.

    def __init__(self, capacity):
        self.capacity = capacity
        self.hm = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_end(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self._remove(node)
        self._add_to_end(node)
        return node.val

    def put(self, key, value):
        if key in self.hm:
            self._remove(self.hm[key])

        node = Node(key, value)
        self.hm[key] = node
        self._add_to_end(node)

        if len(self.hm) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.hm[lru.key]


# --- Test Cases ---
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
print("All test cases passed!")
