def CountWays(s):
    MOD = 10**9 + 7
    n = len(s)
    
    # Edge case: If string is empty, there is one way to decode it.
    if n == 0:
        return 1
    
    # dp array to store the number of ways to decode up to each index
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case for empty string
    
    # For the first character
    dp[1] = 0 if s[0] == '0' else 1
    
    # Fill the dp array
    for i in range(2, n + 1):
        # Single digit decoding
        if s[i-1] != '0':
            dp[i] += dp[i-1]
            dp[i] %= MOD
        
        # Two digit decoding
        if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6'):
            dp[i] += dp[i-2]
            dp[i] %= MOD
    
    return dp[n]

# Example usage:
print(CountWays("123"))  # Output: 3
print(CountWays("90"))   # Output: 0
