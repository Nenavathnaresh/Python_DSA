def isSubsetSum(arr, n, sum):
    # Create a 2D DP array with all False values
    dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
    
    # If sum is 0, the answer is True, since empty subset always works
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    
    return dp[n][sum]

# Example usage:
arr = [3, 34, 4, 12, 5, 2]
n = len(arr)
sum_value = 9

print(1 if isSubsetSum(arr, n, sum_value) else 0)  # Output: 1

sum_value = 30
print(1 if isSubsetSum(arr, n, sum_value) else 0)  # Output: 0
