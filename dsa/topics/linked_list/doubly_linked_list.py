# ============================================================
# Doubly Linked List Implementation
# ============================================================
# A doubly linked list where each node has pointers to both
# the next and previous nodes, allowing O(1) insert/delete
# at any position given a reference to the node.
#
# Operations:
#   - append(val):        Add to end         — O(1)
#   - prepend(val):       Add to front       — O(1)
#   - delete(node):       Remove a node      — O(1)
#   - search(val):        Find first match   — O(n)
#   - display():          Print list         — O(n)
#   - display_reverse():  Print in reverse   — O(n)
# ============================================================


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        """Add node to the end of the list."""
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


    def prepend(self, val):
        """Add node to the front of the list."""
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1


    def delete(self, node):
        """Remove a given node from the list."""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1

    def search(self, val):
        """Return the first node with the given value, or None."""
        node = self.head
        while node:
            if node.val == val:
                return node
            node = node.next
        return None

    def display(self):
        """Print the list from head to tail."""
        vals = []
        node = self.head
        while node:
            vals.append(node.val)
            node = node.next
        return vals

    def display_reverse(self):
        """Print the list from tail to head."""
        vals = []
        node = self.tail
        while node:
            vals.append(node.val)
            node = node.prev
        return vals


# --- Test Cases ---

# Test empty list
dll = DoublyLinkedList()
assert dll.display() == []
assert dll.display_reverse() == []
assert dll.search(1) is None
assert dll.size == 0

# Test append
dll.append(1)
dll.append(2)
dll.append(3)
assert dll.display() == [1, 2, 3]
assert dll.display_reverse() == [3, 2, 1]
assert dll.size == 3

# Test prepend
dll.prepend(0)
dll.prepend(-1)
assert dll.display() == [-1, 0, 1, 2, 3]
assert dll.display_reverse() == [3, 2, 1, 0, -1]
assert dll.size == 5

# Test search
node = dll.search(2)
assert node.val == 2
assert dll.search(99) is None

# Test delete middle node
dll.delete(node)
assert dll.display() == [-1, 0, 1, 3]
assert dll.display_reverse() == [3, 1, 0, -1]
assert dll.size == 4

# Test delete head
head = dll.search(-1)
dll.delete(head)
assert dll.display() == [0, 1, 3]
assert dll.head.val == 0
assert dll.head.prev is None

# Test delete tail
tail = dll.search(3)
dll.delete(tail)
assert dll.display() == [0, 1]
assert dll.tail.val == 1
assert dll.tail.next is None

# Test delete until empty
dll.delete(dll.head)
dll.delete(dll.head)
assert dll.display() == []
assert dll.head is None
assert dll.tail is None
assert dll.size == 0

# Test single element
dll.append(42)
assert dll.head.val == 42
assert dll.tail.val == 42
dll.delete(dll.head)
assert dll.head is None
assert dll.tail is None

print("All test cases passed!")
