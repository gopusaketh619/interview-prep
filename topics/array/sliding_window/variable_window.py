# Example: Smallest subarray with sum >= target
# Given an array of positive integers and a target, 
# find the minimum length of a contiguous subarray 
# whose sum is greater than or equal to the target.
# Return 0 if no such subarray exists.


arr = [2, 1, 5, 2, 3, 2, 5]
target = 7
#→ Output: 2 (subarray [5, 2])


def brute_force(arr, target):

    l = len(arr)
    min_len = float('inf')
    results = []

    for i in range(l):
        curr_sum = 0
        for j in range(i, l):
            curr_sum += arr[j]
            if curr_sum >= target:
                if j-i+1 < min_len:
                    min_len = j-i+1
                    results = [arr[i:j+1]]
                elif min_len == j-i+1:
                    results.append(arr[i:j+1])
    
    return (min_len, results)



def optimal(arr, target):
    left = 0 
    l = len(arr)
    min_len = float('inf')
    summ = 0
    results = []
    
    for right in range(l):
        summ += arr[right]
        if summ >= target:
            while summ >= target:
                if right-left+1 < min_len:
                    min_len = right-left+1
                    results = [arr[left:right+1]]
                elif right-left+1 == min_len:
                    results.append(arr[left:right+1])                
                summ -= arr[left]
                left += 1

    return min_len, results


#print(brute_force(arr, target))
print(optimal(arr, target))
            
