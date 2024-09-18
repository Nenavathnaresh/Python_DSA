def smallestSubarraySum(arr, N):
    # Initialize current sum and minimum sum
    current_sum = 0
    min_sum = arr[0]
    
    for i in range(N):
        # Update the current sum
        current_sum += arr[i]
        
        # Update the minimum sum if current_sum is smaller
        min_sum = min(min_sum, current_sum)
        
        # Reset current_sum if it becomes positive
        if current_sum > 0:
            current_sum = 0
    
    return min_sum

# Example usage:
arr1 = [3, -4, 2, -3, -1, 7, -5]
arr2 = [2, 6, 8, 1, 4]

print(smallestSubarraySum(arr1, len(arr1)))  # Output: -6
print(smallestSubarraySum(arr2, len(arr2)))  # Output: 1
