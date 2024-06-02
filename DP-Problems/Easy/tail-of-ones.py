def numberOfConsecutiveOnes(n):
    MOD = int(1e9+7)
    
    if n == 1:
        return 0

    # Initialize dp arrays
    dp = [[0, 0] for _ in range(n + 1)]
    
    # Base cases
    dp[1][0] = 1
    dp[1][1] = 1
    
    # Fill the dp table
    for i in range(2, n + 1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
        dp[i][1] = dp[i-1][0] % MOD
    
    # Calculate total number of valid strings without consecutive 1's
    valid_strings = (dp[n][0] + dp[n][1]) % MOD
    
    # Total number of binary strings of length n
    total_strings = pow(2, n, MOD)
    
    # Calculate the number of strings with at least one pair of consecutive 1's
    result = (total_strings - valid_strings + MOD) % MOD
    
    return result

# Example usage:
print(numberOfConsecutiveOnes(2))  # Output: 1
print(numberOfConsecutiveOnes(5))  # Output: 19
