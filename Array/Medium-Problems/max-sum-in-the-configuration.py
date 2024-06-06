def maxSum(arr, n):
    # Calculate sum of all array elements
    Sum = sum(arr)
    
    # Calculate initial value of S0
    S0 = sum(i * arr[i] for i in range(n))
    
    # Initialize the maximum sum with S0
    max_sum = S0
    
    # Current value of sum S
    current_val = S0
    
    # Iterate through the array to compute values for rotations
    for i in range(1, n):
        current_val = current_val + Sum - n * arr[n - i]
        if current_val > max_sum:
            max_sum = current_val
    
    return max_sum

# Example usage:
n = 4
arr = [8, 3, 1, 2]
print(maxSum(arr, n))  # Output: 29

n = 3
arr = [1, 2, 3]
print(maxSum(arr, n))  # Output: 8
