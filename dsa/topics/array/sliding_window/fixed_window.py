#Example: Maximum sum of any subarray of size k
# arr = [2, 1, 5, 1, 3, 2], k = 3 
# → Output: 9 (subarray [5, 1, 3])


def brute_force(arr, k):
    max_sum = 0

    for i in range(0, len(arr)-k+1):
        sum = 0
        for j in range(k):
            sum += arr[i+j]
        max_sum = max(max_sum, sum)
    return max_sum 


def optimized(arr, k):
    l = len(arr)
    if l < k:
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, l):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3 

print(brute_force(arr, k))

print(optimized(arr, k))

