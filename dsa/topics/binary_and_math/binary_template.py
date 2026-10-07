# ============================================================
# BIT MANIPULATION / MATH - PATTERN TEMPLATE
# ============================================================
#
# Bit manipulation uses binary representations and bitwise
# operators for efficient computation.
#
# BITWISE OPERATORS:
#   &   AND        (both bits 1)
#   |   OR         (either bit 1)
#   ^   XOR        (bits differ)
#   ~   NOT        (flip all bits)
#   <<  Left shift  (multiply by 2)
#   >>  Right shift (divide by 2)
#
# COMMON TRICKS:
#
#   x & 1              # check if odd (last bit is 1)
#   x >> 1             # x // 2
#   x << 1             # x * 2
#   x & (x - 1)        # clear lowest set bit
#   x & (-x)           # isolate lowest set bit
#   x | (1 << i)       # set bit at position i
#   x & ~(1 << i)      # clear bit at position i
#   x ^ x == 0         # XOR with self = 0
#   a ^ b ^ a == b     # XOR cancels duplicates
#
# PATTERNS:
#
#   1. Single Number (find unique among duplicates):
#      XOR all elements — duplicates cancel out.
#
#   2. Power of 2 check:
#      n > 0 and (n & (n-1)) == 0
#
#   3. Count set bits (Hamming weight):
#      count = 0
#      while n:
#          n &= (n - 1)  # clear lowest set bit
#          count += 1
#
#   4. Subset enumeration with bitmask:
#      for mask in range(1 << n):
#          subset = [arr[i] for i in range(n) if mask & (1 << i)]
#
# MATH PATTERNS:
#   - GCD: math.gcd(a, b)
#   - Modular arithmetic: pow(base, exp, mod)
#   - Integer overflow: not an issue in Python (arbitrary precision)
#
# WHEN TO USE:
#   - "Single number among duplicates" → XOR
#   - "Power of 2" → bit check
#   - "Count bits" → Brian Kernighan's
#   - "Generate all subsets" → bitmask
#   - Space optimization (boolean array → bitmask)
#
# TIME: O(1) per bit operation (O(32) = O(1) for 32-bit ints)
# SPACE: O(1)
# ============================================================
