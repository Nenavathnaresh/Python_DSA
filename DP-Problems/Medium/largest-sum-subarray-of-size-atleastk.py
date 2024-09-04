def maxSumWithK(a, n, k):
    # Array to store max sum of subarrays ending at index i
    max_sum = [0] * n
    
    # Calculate the max sum subarray ending at each index
    current_sum = a[0]
    max_sum[0] = current_sum
    
    for i in range(1, n):
        current_sum = max(a[i], current_sum + a[i])
        max_sum[i] = current_sum
    
    # Now consider subarrays of at least length k
    sum_k = sum(a[:k])
    result = sum_k
    
    for i in range(k, n):
        sum_k += a[i] - a[i - k]
        result = max(result, sum_k, sum_k + max_sum[i - k])
    
    return result

# Example usage:
n = 4
a = [1, -2, 2, -3]
k = 2
print(maxSumWithK(a, n, k))  # Output: 1

n = 6
a = [1, 1, 1, 1, 1, 1]
k = 2
print(maxSumWithK(a, n, k))  # Output: 6
