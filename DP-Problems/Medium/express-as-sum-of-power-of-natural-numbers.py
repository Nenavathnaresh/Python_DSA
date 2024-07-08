def numOfWays(n, x):
    MOD = 10**9 + 7
    
    # Find the maximum value of k such that k^x <= n
    max_base = int(n**(1/x))
    
    # Create a dp table
    dp = [[0 for _ in range(max_base + 1)] for _ in range(n + 1)]
    
    # Base case
    for j in range(max_base + 1):
        dp[0][j] = 1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, max_base + 1):
            power = j ** x
            if i >= power:
                dp[i][j] = (dp[i][j-1] + dp[i-power][j-1]) % MOD
            else:
                dp[i][j] = dp[i][j-1]
    
    # The answer is the number of ways to form n using numbers 1 to max_base
    return dp[n][max_base]

# Example usage
print(numOfWays(10, 2))  # Output: 1
print(numOfWays(100, 2)) # Output: 3
