def fillingBucket(N):
    # Define the modulo
    MOD = 100000000
    
    # Initialize dp array
    dp = [0] * (N + 1)
    
    # Base cases
    dp[0] = 1
    dp[1] = 1
    
    # Fill the dp array using the recursive relation
    for i in range(2, N + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[N]

# Example usage
N = 4
print(fillingBucket(N))  # Output: 5

N = 3
print(fillingBucket(N))  # Output: 3

#######################################################################

def fillingBucket(N):
    MOD = 10**8
    
    # Base cases
    if N == 0:
        return 1
    if N == 1:
        return 1
    
    # Only store the last two values
    prev2 = 1  # dp[0]
    prev1 = 1  # dp[1]
    
    # Compute dp[i] for i = 2 to N using two variables
    for i in range(2, N + 1):
        current = (prev1 + prev2) % MOD
        prev2 = prev1
        prev1 = current
    
    return prev1

# Example usage:
print(fillingBucket(3))  # Output: 3
print(fillingBucket(4))  # Output: 5
