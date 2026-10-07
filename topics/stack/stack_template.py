# ============================================================
# STACK - PATTERN TEMPLATE
# ============================================================
#
# A stack is a LIFO (Last In, First Out) data structure.
# In Python, use a list: append() to push, pop() to pop.
#
# BASIC OPERATIONS:
#   stack = []
#   stack.append(x)    # push O(1)
#   stack.pop()        # pop O(1)
#   stack[-1]          # peek O(1)
#   len(stack) == 0    # is_empty
#
# KEY TECHNIQUES:
#
#   1. Matching Parentheses:
#      Push opening brackets, pop on closing brackets.
#      If mismatch or stack not empty at end → invalid.
#
#   2. Monotonic Stack (Next Greater Element):
#      Maintain stack in decreasing order.
#      When new element > stack top, pop and record answer.
#
#      stack = []
#      result = [-1] * n
#      for i in range(n):
#          while stack and arr[stack[-1]] < arr[i]:
#              result[stack.pop()] = arr[i]
#          stack.append(i)
#
#   3. Expression Evaluation (Postfix/RPN):
#      Push operands. On operator, pop two, compute, push result.
#
#   4. Iterative DFS:
#      Use stack instead of recursion for tree/graph DFS.
#
# WHEN TO USE:
#   - Matching/nesting problems (brackets, HTML tags)
#   - Next greater/smaller element
#   - Expression parsing/evaluation
#   - Undo/redo operations
#   - Iterative DFS traversal
#   - Histogram problems
#
# TIME: O(1) per push/pop/peek
# SPACE: O(n) for n elements in stack
# ============================================================
