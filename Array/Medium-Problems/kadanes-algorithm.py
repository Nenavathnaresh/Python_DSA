def maxSubArraySum(arr):
    # Initialize variables
    max_sum = float('-inf')  # To handle all negative numbers case
    current_sum = 0
    
    for num in arr:
        current_sum += num
        
        # Update max_sum if current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
        
        # If current_sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

# Example usage:
arr1 = [1, 2, 3, -2, 5]
arr2 = [-1, -2, -3, -4]
arr3 = [5, 4, 7]

print(maxSubArraySum(arr1))  # Output: 9
print(maxSubArraySum(arr2))  # Output: -1
print(maxSubArraySum(arr3))  # Output: 16
