MOD = 10**9 + 7

def bellNumber(N):
    # Create a DP table with dimensions (N+1) x (N+1)
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Base case: B(0) = 1
    dp[0][0] = 1
    
    # Fill the DP table using the recursive relation
    for i in range(1, N+1):
        # Bell number relation: dp[i][0] = dp[i-1][i-1]
        dp[i][0] = dp[i-1][i-1]
        
        # Fill the rest using the recurrence relation
        for j in range(1, i+1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) % MOD
    
    # The Bell number for n is dp[N][0]
    return dp[N][0]
