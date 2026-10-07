# ============================================================
# PROBLEM: Design Circular Queue
# LeetCode: 622 | https://leetcode.com/problems/design-circular-queue/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Design your implementation of a circular queue. A circular
# queue is a linear data structure that uses FIFO principle
# and the last position is connected back to the first (ring buffer).
#
# Constraints:
#   - 1 <= k <= 1000
#   - 0 <= value <= 1000
#   - At most 3000 calls to enQueue, deQueue, Front, Rear, isEmpty, isFull
#
# Examples:
#   Input:  MyCircularQueue(3), enQueue(1) -> True, enQueue(2) -> True
#           enQueue(3) -> True, enQueue(4) -> False, Rear() -> 3
# ============================================================

class MyCircularQueue:
    # Pattern: <pattern>
    # Time: O(?) per operation | Space: O(?)
    #
    # Approach:
    #   1. <step>

    def __init__(self, k):
        pass

    def en_queue(self, value):
        pass

    def de_queue(self):
        pass

    def front(self):
        pass

    def rear(self):
        pass

    def is_empty(self):
        pass

    def is_full(self):
        pass


# --- Test Cases ---
cq = MyCircularQueue(3)
assert cq.en_queue(1) == True
assert cq.en_queue(2) == True
assert cq.en_queue(3) == True
assert cq.en_queue(4) == False
assert cq.rear() == 3
assert cq.is_full() == True
print("All test cases passed!")
