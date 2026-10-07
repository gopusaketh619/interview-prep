# ============================================================
# PROBLEM: Min Stack
# LeetCode: 155 | https://leetcode.com/problems/min-stack/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Design a stack that supports push, pop, top, and retrieving
# the minimum element in constant time.
#   - push(val): Pushes val onto the stack.
#   - pop(): Removes the element on the top.
#   - top(): Gets the top element.
#   - getMin(): Retrieves the minimum element.
#
# Constraints:
#   - -2^31 <= val <= 2^31 - 1
#   - pop, top, and getMin are always called on non-empty stacks
#   - At most 3 * 10^4 calls to push, pop, top, and getMin
#
# Examples:
#   Input:  push(-2), push(0), push(-3), getMin() -> -3
#           pop(), top() -> 0, getMin() -> -2
# ============================================================

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def getMin(self):
        pass


# --- Test Cases ---
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
assert ms.getMin() == -3
ms.pop()
assert ms.top() == 0
assert ms.getMin() == -2

ms2 = MinStack()
ms2.push(1)
ms2.push(2)
assert ms2.getMin() == 1
ms2.push(-1)
assert ms2.getMin() == -1
ms2.pop()
assert ms2.getMin() == 1

print("All test cases passed!")
