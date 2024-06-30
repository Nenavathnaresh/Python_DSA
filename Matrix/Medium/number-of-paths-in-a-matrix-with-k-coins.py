def numberOfPath(n, k, arr):
    # Initialize the dp array
    dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
    
    # Initialize starting point
    if arr[0][0] <= k:
        dp[0][0][arr[0][0]] = 1
    
    # Fill dp array
    for i in range(n):
        for j in range(n):
            for coins in range(k + 1):
                if dp[i][j][coins] > 0:
                    # Move down
                    if i + 1 < n and coins + arr[i + 1][j] <= k:
                        dp[i + 1][j][coins + arr[i + 1][j]] += dp[i][j][coins]
                    # Move right
                    if j + 1 < n and coins + arr[i][j + 1] <= k:
                        dp[i][j + 1][coins + arr[i][j + 1]] += dp[i][j][coins]
    
    # Return the number of ways to collect exactly k coins at the bottom-right corner
    return dp[n - 1][n - 1][k]

# Example usage
k = 12
n = 3
arr = [
    [1, 2, 3], 
    [4, 6, 5], 
    [3, 2, 1]
]
print(numberOfPath(n, k, arr))  # Output: 2

k = 16
n = 3
arr = [
    [1, 2, 3], 
    [4, 6, 5], 
    [9, 8, 7]
]
print(numberOfPath(n, k, arr))  # Output: 0
