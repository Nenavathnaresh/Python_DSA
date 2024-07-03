def optimalKeys(N):
    if N <= 6:
        return N
    
    dp = [0] * (N + 1)
    
    for i in range(1, 7):
        dp[i] = i
        
    for i in range(7, N + 1):
        for j in range(i - 3, 0, -1):
            dp[i] = max(dp[i], dp[j] * (i - j - 1))
    
    return dp[N]

# Test cases
print(optimalKeys(3))  # Output: 3
print(optimalKeys(7))  # Output: 9
