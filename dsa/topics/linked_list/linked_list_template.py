# ============================================================
# LINKED LIST - PATTERN TEMPLATE
# ============================================================
#
# A linked list is a linear data structure where each element
# (node) contains a value and a pointer to the next node.
# No random access — must traverse from head.
#
# NODE DEFINITION:
#   class ListNode:
#       def __init__(self, val=0, next=None):
#           self.val = val
#           self.next = next
#
# KEY TECHNIQUES:
#
#   1. Fast/Slow Pointer (Floyd's):
#      - Cycle detection: fast moves 2x, slow moves 1x
#      - Find middle: when fast reaches end, slow is at middle
#
#      slow = fast = head
#      while fast and fast.next:
#          slow = slow.next
#          fast = fast.next.next
#      # slow is now at the middle
#
#   2. Reversal (Iterative):
#      prev, curr = None, head
#      while curr:
#          next_node = curr.next
#          curr.next = prev
#          prev = curr
#          curr = next_node
#      return prev  # new head
#
#   3. Dummy Head (simplifies edge cases):
#      dummy = ListNode(0)
#      dummy.next = head
#      # ... operations ...
#      return dummy.next
#
#   4. Merge Two Sorted Lists:
#      Use a dummy node and two pointers, appending the
#      smaller value each step.
#
# WHEN TO USE:
#   - In-place reversal
#   - Cycle detection
#   - Merge/split operations
#   - Remove nth from end (two pointers with gap)
#   - Detect intersection point
#
# COMMON MISTAKES:
#   - Losing reference to head (use dummy)
#   - Not handling null/empty list
#   - Infinite loops from incorrect pointer updates
#
# TIME: O(n) for most operations (traversal required)
# SPACE: O(1) for iterative, O(n) for recursive
# ============================================================


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked(arr):
    """Helper: convert list to linked list."""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_to_list(head):
    """Helper: convert linked list to list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
