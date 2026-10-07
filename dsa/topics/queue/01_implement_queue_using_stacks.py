# ============================================================
# PROBLEM: Implement Queue using Stacks
# LeetCode: 232 | https://leetcode.com/problems/implement-queue-using-stacks/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Implement a first-in-first-out (FIFO) queue using only two
# stacks. The implemented queue should support push, peek,
# pop, and empty operations.
#
# Constraints:
#   - 1 <= x <= 9
#   - At most 100 calls to push, pop, peek, and empty
#   - All calls to pop and peek are valid
#
# Examples:
#   Input:  push(1), push(2), peek() -> 1, pop() -> 1, empty() -> False
# ============================================================

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def empty(self):
        pass

    def _transfer(self):
        pass


# --- Test Cases ---
q = MyQueue()
q.push(1)
q.push(2)
assert q.peek() == 1
assert q.pop() == 1
assert q.empty() == False
assert q.pop() == 2
assert q.empty() == True

q2 = MyQueue()
q2.push(10)
q2.push(20)
q2.push(30)
assert q2.pop() == 10
q2.push(40)
assert q2.pop() == 20
assert q2.pop() == 30
assert q2.pop() == 40

print("All test cases passed!")
