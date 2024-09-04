def TotalWays(N):
    MOD = 10**9 + 7
    
    # Base cases
    if N == 1:
        return 4
    
    # dp array to store the number of ways for one side
    dp = [0] * (N + 1)
    
    # Initialize base cases
    dp[0] = 1
    dp[1] = 2
    
    # Fill dp array for all plots up to N
    for i in range(2, N + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    # Result is the square of dp[N] modulo MOD
    result = (dp[N] * dp[N]) % MOD
    return result

# Example usage:
N = 3
print(TotalWays(N))  # Output: 25
