def countSubarray(arr, n, k):
    total_subarrays = n * (n + 1) // 2  # Total number of subarrays
    count_leq_k = 0  # To count subarrays where all elements are <= K
    current_count = 0  # To track the length of contiguous subarrays where elements are <= K

    for i in range(n):
        if arr[i] <= k:
            current_count += 1
        else:
            # When we hit an element > K, add the count of subarrays formed by the previous subarrays <= K
            count_leq_k += current_count * (current_count + 1) // 2
            current_count = 0  # Reset the count for next contiguous subarrays <= K
    
    # Add the remaining subarrays formed by the last contiguous elements <= K
    count_leq_k += current_count * (current_count + 1) // 2

    # The number of subarrays with max element > K is total subarrays minus those where all elements <= K
    return total_subarrays - count_leq_k

# Example Usage
print(countSubarray([3, 2, 1], 3, 2))  # Output: 3
print(countSubarray([1, 2, 3, 4], 4, 1))  # Output: 9
