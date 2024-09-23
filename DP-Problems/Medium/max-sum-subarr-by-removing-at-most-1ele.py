def maxSumWithOneSkip(arr):
    n = len(arr)
    
    if n == 0:
        return 0
    
    # Initialize the DP arrays
    dp_no_skip = [0] * n
    dp_skip = [0] * n
    
    # Base case
    dp_no_skip[0] = arr[0]
    dp_skip[0] = arr[0]
    
    max_sum = arr[0]
    
    # Fill the DP arrays
    for i in range(1, n):
        dp_no_skip[i] = max(arr[i], dp_no_skip[i-1] + arr[i])
        dp_skip[i] = max(dp_no_skip[i-1], dp_skip[i-1] + arr[i])
        
        # Keep track of the maximum sum found
        max_sum = max(max_sum, dp_no_skip[i], dp_skip[i])
    
    return max_sum

# Example usage:
arr1 = [1, 2, 3, -4, 5]
print(maxSumWithOneSkip(arr1))  # Output: 11

arr2 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSumWithOneSkip(arr2))  # Output: 9
