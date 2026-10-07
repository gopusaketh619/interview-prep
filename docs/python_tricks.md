# Python Tricks for DSA

Quick reference for Python-specific patterns, built-ins, and idioms commonly used in coding interviews.

---

## Collections Module

### Counter — Frequency Map in One Line

```python
from collections import Counter

Counter("aabbc")          # Counter({'a': 2, 'b': 2, 'c': 1})
Counter([1, 1, 2, 3])    # Counter({1: 2, 2: 1, 3: 1})

c = Counter("aabbbcccc")
c['a']                    # 2
c['z']                    # 0 (no KeyError for missing keys!)
c.most_common(2)          # [('c', 4), ('b', 3)]

# Arithmetic
a = Counter("aabb")
b = Counter("abcc")
a + b                     # Counter({'a': 3, 'b': 3, 'c': 2})
a - b                     # Counter({'a': 1, 'b': 1}) — drops zero/negative
a & b                     # Counter({'a': 1, 'b': 1}) — min of each
a | b                     # Counter({'a': 2, 'b': 2, 'c': 2}) — max of each

# Check anagram
Counter("listen") == Counter("silent")  # True

# Check for duplicates
any(v > 1 for v in Counter(s).values())
```

### deque — O(1) Append/Pop from Both Ends

```python
from collections import deque

dq = deque()
dq.append(1)        # add to right: [1]
dq.appendleft(0)    # add to left: [0, 1]
dq.pop()            # remove from right: [0]
dq.popleft()        # remove from left: []

# BFS queue
queue = deque([start_node])
while queue:
    node = queue.popleft()  # O(1) — DON'T use list.pop(0) which is O(n)

# Sliding window with max size
dq = deque(maxlen=k)  # auto-drops oldest when full
```

### defaultdict — Dict with Default Values

```python
from collections import defaultdict

graph = defaultdict(list)
graph['a'].append('b')    # no need to check if 'a' exists

freq = defaultdict(int)
freq['x'] += 1            # starts at 0, no KeyError

groups = defaultdict(set)
groups['key'].add('val')
```

---

## Heap (heapq) — Priority Queue

```python
import heapq

# Min-heap (default)
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappop(heap)       # returns 2 (smallest)

# Max-heap trick: negate values
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)

# Heapify a list in-place: O(n)
arr = [5, 2, 8, 1, 9]
heapq.heapify(arr)        # arr is now a valid min-heap

# Top-K largest/smallest
heapq.nlargest(3, arr)    # [9, 8, 5]
heapq.nsmallest(3, arr)   # [1, 2, 5]

# Heap with tuples (sorts by first element)
heapq.heappush(heap, (distance, node))  # useful for Dijkstra
```

---

## String Operations

### Immutability — Strings Cannot Be Modified In-Place

```python
# BAD: O(n²) for n concatenations
word = ""
for ch in chars:
    word += ch      # creates new string each time!

# GOOD: O(n) using list + join
parts = []
for ch in chars:
    parts.append(ch)  # O(1) amortized
result = "".join(parts)  # O(n) single copy
```

### Slicing — End Index is Exclusive

```python
s = "abcdef"
s[0:3]    # "abc"   (indices 0, 1, 2)
s[2:5]    # "cde"   (indices 2, 3, 4)
s[0:6]    # "abcdef" (full string — need len(s) to include last char)
s[::-1]   # "fedcba" (reversed)
s[::2]    # "ace"   (every 2nd char)
```

### Useful String Methods

```python
s.isalnum()       # True if all alphanumeric
s.isalpha()       # True if all letters
s.isdigit()       # True if all digits
s.lower()         # lowercase copy
s.strip()         # remove leading/trailing whitespace
ord('a')          # 97 (ASCII value)
chr(97)           # 'a'
ord(c) - ord('a') # position 0-25 for lowercase letters
```

---

## Sorting

```python
# Sort in-place
arr.sort()                          # ascending
arr.sort(reverse=True)              # descending
arr.sort(key=lambda x: x[1])       # by second element
arr.sort(key=lambda x: (-x[0], x[1]))  # multi-key

# Sorted (returns new list, doesn't modify original)
sorted(arr)
sorted(arr, key=len)               # by length
sorted(s)                          # sorts string chars → list

# Sort stability: Python's sort is stable (equal elements keep original order)
```

---

## Binary Search with bisect

```python
import bisect

arr = [1, 3, 5, 7, 9]
bisect.bisect_left(arr, 5)    # 2 — leftmost position to insert 5
bisect.bisect_right(arr, 5)   # 3 — rightmost position to insert 5
bisect.insort(arr, 4)         # inserts 4 in sorted position → [1, 3, 4, 5, 7, 9]

# Find first occurrence of target
idx = bisect.bisect_left(arr, target)
if idx < len(arr) and arr[idx] == target:
    return idx  # found
```

---

## Common Patterns

### Infinity as Sentinel

```python
min_val = float('inf')     # positive infinity
max_val = float('-inf')    # negative infinity

# Useful for min/max tracking
for x in arr:
    min_val = min(min_val, x)
```

### Dictionary Tricks

```python
# Increment or initialize
d[key] = d.get(key, 0) + 1

# Delete key safely
d.pop(key, None)           # returns None if missing (no KeyError)

# Delete when count reaches 0 (common in sliding window)
d[key] -= 1
if d[key] == 0:
    del d[key]

# Iterate items
for key, val in d.items():
    pass
```

### Set Operations

```python
s = set()
s.add(x)           # O(1)
s.remove(x)        # O(1), raises KeyError if missing
s.discard(x)       # O(1), no error if missing
x in s             # O(1) lookup

# Set math
a | b              # union
a & b              # intersection
a - b              # difference
a ^ b              # symmetric difference
```

### List as Stack

```python
stack = []
stack.append(x)    # push — O(1)
stack.pop()        # pop from top — O(1)
stack[-1]          # peek at top — O(1)
```

### Enumerate and Zip

```python
for i, val in enumerate(arr):     # index + value
    pass

for a, b in zip(arr1, arr2):     # parallel iteration
    pass
```

### Tuple Unpacking

```python
# Swap without temp
a, b = b, a

# Unpack in loop
intervals = [[1,3], [2,6], [8,10]]
for start, end in intervals:
    pass
```

---

## Math Shortcuts

```python
# Integer division (floors toward negative infinity in Python)
7 // 2         # 3
-7 // 2        # -4

# Ceiling division
-(-n // d)     # ceiling of n/d
(n + d - 1) // d  # also ceiling (for positive n, d)

# Power / modular arithmetic
pow(base, exp, mod)  # (base^exp) % mod — efficient

# GCD
from math import gcd
gcd(12, 8)     # 4

# Check power of 2
n > 0 and (n & (n - 1)) == 0
```

---

## Bit Manipulation

```python
x & 1           # 1 if odd, 0 if even
x >> 1          # x // 2
x << 1          # x * 2
x & (x - 1)    # clear lowest set bit (also counts if power of 2)
x | (1 << i)   # set bit i
x & ~(1 << i)  # clear bit i
x ^ y           # XOR — same bits cancel out
bin(x).count('1')  # count set bits
```

---

## Recursion Helpers

```python
import sys
sys.setrecursionlimit(10000)  # increase if needed (default ~1000)

# Memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
