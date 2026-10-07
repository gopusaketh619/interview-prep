# ============================================================
# PROBLEM: All O`one Data Structure
# LeetCode: 432 | https://leetcode.com/problems/all-oone-data-structure/
# Difficulty: Hard | Time to Solve: 35 min
# ============================================================
# Design a data structure to store strings' count with the ability
# to return the strings with minimum and maximum counts.
#   - inc(key): Increments the count of key by 1.
#   - dec(key): Decrements the count of key by 1. Remove if count is 0.
#   - getMaxKey(): Returns a key with the maximum count.
#   - getMinKey(): Returns a key with the minimum count.
# Each function must run in O(1) average time.
#
# Constraints:
#   - 1 <= key.length <= 10
#   - key consists of lowercase English letters
#   - At most 5 * 10^4 calls to inc, dec, getMaxKey, getMinKey
#   - It is guaranteed dec will only be called on existing keys
#
# Examples:
#   Input:  inc("hello"), inc("hello"), getMaxKey() -> "hello"
#           inc("leet"), getMinKey() -> "leet"
# ============================================================


class Node:
    """Each node represents a bucket holding all keys with the same count."""
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    # Pattern: Doubly linked list (sorted by count) + two hashmaps
    # Time: O(1) per operation | Space: O(n)
    #
    # Approach:
    #   - key_count: key -> current count
    #   - count_node: count -> linked list node (bucket)
    #   - Doubly linked list of buckets sorted by count:
    #       head <-> [min count bucket] <-> ... <-> [max count bucket] <-> tail
    #   - inc: move key from its current bucket to the next bucket (count+1)
    #   - dec: move key from its current bucket to the prev bucket (count-1)
    #   - getMax: return any key from tail.prev
    #   - getMin: return any key from head.next
    #
    # Key insight: Since inc/dec only change count by 1, the target bucket
    # is always adjacent to the current one (or needs to be created adjacent).
    # This guarantees O(1) — no searching needed.

    def __init__(self):
        self.key_count = {}       # key -> its current count
        self.count_node = {}      # count -> the linked list node for that count
        self.head = Node(0)       # dummy head (sentinel)
        self.tail = Node(0)       # dummy tail (sentinel)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, prev_node, new_node):
        """Insert new_node right after prev_node."""
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.count_node[new_node.count] = new_node

    def _remove_node(self, node):
        """Unlink node from the list and remove from count_node map."""
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def inc(self, key):
        if key in self.key_count:
            old_count = self.key_count[key]
            new_count = old_count + 1
            self.key_count[key] = new_count

            old_node = self.count_node[old_count]

            # Create new_count bucket if it doesn't exist (insert right of old)
            if new_count not in self.count_node:
                self._insert_after(old_node, Node(new_count))

            self.count_node[new_count].keys.add(key)

            # Remove key from old bucket, delete bucket if empty
            old_node.keys.remove(key)
            if not old_node.keys:
                self._remove_node(old_node)
        else:
            # Brand new key, count becomes 1
            self.key_count[key] = 1

            if 1 not in self.count_node:
                self._insert_after(self.head, Node(1))

            self.count_node[1].keys.add(key)

    def dec(self, key):
        old_count = self.key_count[key]
        new_count = old_count - 1

        old_node = self.count_node[old_count]

        if new_count == 0:
            # Key is removed entirely
            del self.key_count[key]
        else:
            # Move key to the count-1 bucket (create left of old if needed)
            self.key_count[key] = new_count
            if new_count not in self.count_node:
                self._insert_after(old_node.prev, Node(new_count))
            self.count_node[new_count].keys.add(key)

        # Remove key from old bucket, delete bucket if empty
        old_node.keys.remove(key)
        if not old_node.keys:
            self._remove_node(old_node)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# --- Test Cases ---
obj = AllOne()

# Empty state
assert obj.getMaxKey() == ""
assert obj.getMinKey() == ""

# Single key inc
obj.inc("hello")
assert obj.getMaxKey() == "hello"
assert obj.getMinKey() == "hello"

# Inc same key again
obj.inc("hello")
assert obj.getMaxKey() == "hello"
assert obj.getMinKey() == "hello"

# Add second key (lower count = new min)
obj.inc("leet")
assert obj.getMaxKey() == "hello"
assert obj.getMinKey() == "leet"

# Dec max key — both now at count 1
obj.dec("hello")
assert obj.getMinKey() in ("hello", "leet")

# Dec to remove hello entirely
obj.dec("hello")
assert obj.getMaxKey() == "leet"
assert obj.getMinKey() == "leet"

# Dec last key — back to empty
obj.dec("leet")
assert obj.getMaxKey() == ""
assert obj.getMinKey() == ""

# Stress test: multiple keys at various counts
obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("c")
obj.inc("c")
obj.inc("c")
assert obj.getMaxKey() == "c"
assert obj.getMinKey() == "a"

obj.inc("a")
obj.inc("a")
obj.inc("a")
assert obj.getMaxKey() == "a"

obj.dec("a")
obj.dec("a")
assert obj.getMaxKey() == "c"

print("All test cases passed!")
