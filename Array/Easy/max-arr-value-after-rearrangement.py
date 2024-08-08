def max_sum(arr):
    MOD = 10**9 + 7
    # Sort the array
    arr.sort()
    
    # Calculate the maximum sum
    max_value = 0
    for i in range(len(arr)):
        max_value = (max_value + arr[i] * i) % MOD
    
    return max_value

# Example Usage
arr1 = [5, 3, 2, 4, 1]
arr2 = [1, 2, 3]

print(max_sum(arr1))  # Output: 40
print(max_sum(arr2))  # Output: 8
