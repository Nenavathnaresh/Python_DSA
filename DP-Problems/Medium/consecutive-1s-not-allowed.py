def countStrings(N):
    MOD = 1000000007
    
    if N == 1:
        return 2
    
    # dp[i][0] -> valid strings of length i ending in 0
    # dp[i][1] -> valid strings of length i ending in 1
    dp0, dp1 = 1, 1  # For N = 1
    
    for i in range(2, N + 1):
        new_dp0 = (dp0 + dp1) % MOD
        new_dp1 = dp0 % MOD
        
        dp0 = new_dp0
        dp1 = new_dp1
    
    return (dp0 + dp1) % MOD

# Example usage:
N = 3
print(countStrings(N))  # Output: 5
