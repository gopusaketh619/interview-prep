# ============================================================
# PREFIX SUM - PATTERN TEMPLATE
# ============================================================
#
# Prefix sum is a precomputation technique where you build an
# array where prefix[i] = sum of elements from index 0 to i.
# This allows any subarray sum to be computed in O(1).
#
# BUILDING PREFIX SUM:
#   prefix = [0] * (n + 1)
#   for i in range(n):
#       prefix[i+1] = prefix[i] + nums[i]
#
# QUERYING SUBARRAY SUM [i..j]:
#   sum(i, j) = prefix[j+1] - prefix[i]
#
# WHEN TO USE:
#   - Need multiple subarray sum queries
#   - "Subarray with sum equal to k"
#   - "Number of subarrays with sum equal to k"
#   - Product of array except self
#   - Running totals, cumulative frequency
#
# VARIANTS:
#   - Prefix product
#   - Suffix sum / suffix product
#   - Prefix XOR
#   - 2D prefix sum (matrix region queries)
#
# TIME: O(n) to build, O(1) per query
# SPACE: O(n) for the prefix array
# ============================================================
