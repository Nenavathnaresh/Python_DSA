def maxMeritPoints(n, arr):
    # dp table
    dp = [[0] * 3 for _ in range(n)]
    
    # Initialize the first day's activities
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]
    dp[0][2] = arr[0][2]
    
    # Fill the dp table for subsequent days
    for i in range(1, n):
        dp[i][0] = arr[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + max(dp[i-1][0], dp[i-1][1])
    
    # The result will be the max value on the last day
    return max(dp[n-1][0], dp[n-1][1], dp[n-1][2])

# Example usage:
n = 3
arr = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
print(maxMeritPoints(n, arr))  # Output: 11
