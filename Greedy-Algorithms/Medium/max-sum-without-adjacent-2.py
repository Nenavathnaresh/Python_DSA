def findMaxSum(arr, n):
    # Edge cases for arrays of size 1, 2, or 3
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return arr[0] + arr[1]
    elif n == 3:
        return max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    
    # Initialize the dp array
    dp = [0] * n
    
    # Base cases
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2])
    
    # Fill the dp array using the recurrence relation
    for i in range(3, n):
        dp[i] = max(dp[i-1], 
                    arr[i] + dp[i-2], 
                    arr[i] + arr[i-1] + dp[i-3])
    
    # The answer will be in dp[n-1]
    return dp[n-1]

# Example usage:
arr1 = [1, 2, 3]
print(findMaxSum(arr1, len(arr1)))  # Output: 5

arr2 = [3000, 2000, 1000, 3, 10]
print(findMaxSum(arr2, len(arr2)))  # Output: 5013
