# ============================================================
# PROBLEM: Linked List Cycle
# LeetCode: 141 | https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given head of a linked list, determine if the linked list
# has a cycle in it. A cycle exists if some node can be
# reached again by continuously following the next pointer.
#
# Constraints:
#   - The number of nodes is in the range [0, 10^4]
#   - -10^5 <= Node.val <= 10^5
#
# Examples:
#   Input:  head = [3, 2, 0, -4], pos = 1 (cycle at index 1)
#   Output: True
#
#   Input:  head = [1, 2], pos = -1 (no cycle)
#   Output: False
# ============================================================

from linked_list_template import ListNode


def has_cycle(head):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def has_cycle_set(head):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
# Create cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle at node 2)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # cycle

assert has_cycle(node1) == True
assert has_cycle_set(node1) == True

# No cycle: 1 -> 2 -> 3
node_a = ListNode(1)
node_b = ListNode(2)
node_c = ListNode(3)
node_a.next = node_b
node_b.next = node_c

assert has_cycle(node_a) == False
assert has_cycle(None) == False

print("All test cases passed!")
