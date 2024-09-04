def findCatalan(N):
    MOD = int(1e9 + 7)
    
    # Initialize a list to store the catalan numbers
    dp = [0] * (N + 1)
    
    # Base case
    dp[0] = 1
    
    # Fill the dp array using the recursive relation
    for i in range(1, N + 1):
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
            dp[i] %= MOD  # Taking mod to prevent overflow
    
    return dp[N]

# Example usage:
print(findCatalan(3))  # Output: 5
print(findCatalan(4))  # Output: 14
