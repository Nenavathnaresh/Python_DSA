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

##########################################################################################

def maxSubArraySum(arr):
    # Initialize current_sum and max_sum with the first element
    current_sum = max_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Update current_sum, starting a new subarray if necessary
        current_sum = max(arr[i], current_sum + arr[i])
        # Update max_sum if current_sum is higher
        max_sum = max(max_sum, current_sum)
    
    return max_sum
###################################################################################################

def maxSubArraySumDP(arr):
    n = len(arr)
    
    # Initialize dp array
    dp = [0] * n
    
    # Base case
    dp[0] = arr[0]
    
    # Fill dp array
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    
    # The result will be the maximum value in dp array
    return max(dp)

# Example usage
arr1 = [1, 2, 3, -2, 5]
arr2 = [-1, -2, -3, -4]
arr3 = [5, 4, 7]

print(maxSubArraySumDP(arr1))  # Output: 9
print(maxSubArraySumDP(arr2))  # Output: -1
print(maxSubArraySumDP(arr3))  # Output: 16

