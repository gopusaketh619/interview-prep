# ============================================================
# PROBLEM: Implement Stack using Queues
# LeetCode: 225 | https://leetcode.com/problems/implement-stack-using-queues/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Implement a last-in-first-out (LIFO) stack using only two
# queues. The implemented stack should support push, top,
# pop, and empty operations.
#
# Constraints:
#   - 1 <= x <= 9
#   - At most 100 calls to push, pop, top, and empty
#   - All calls to pop and top are valid
#
# Examples:
#   Input:  push(1), push(2), top() -> 2, pop() -> 2, empty() -> False
# ============================================================

from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def empty(self):
        pass


# --- Test Cases ---
s = MyStack()
s.push(1)
s.push(2)
assert s.top() == 2
assert s.pop() == 2
assert s.empty() == False
assert s.pop() == 1
assert s.empty() == True

s2 = MyStack()
s2.push(10)
s2.push(20)
s2.push(30)
assert s2.pop() == 30
assert s2.pop() == 20
assert s2.pop() == 10

print("All test cases passed!")
