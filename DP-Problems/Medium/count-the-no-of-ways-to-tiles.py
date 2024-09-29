MOD = 10**9 + 7

def countWays(n, m):
    # Initialize dp array with zeros
    dp = [0] * (n + 1)
    
    # Base cases
    for i in range(1, min(m, n) + 1):
        dp[i] = 1  # When i < m, only one way to place tiles horizontally
    if n >= m:
        dp[m] = 2  # When i == m, two ways: all horizontal or all vertical
    
    # Fill the dp array for larger values of n
    for i in range(m + 1, n + 1):
        dp[i] = (dp[i - 1] + dp[i - m]) % MOD
    
    return dp[n]

# Example usage:
n1, m1 = 2, 3
print(countWays(n1, m1))  # Output: 1

n2, m2 = 4, 4
print(countWays(n2, m2))  # Output: 2
