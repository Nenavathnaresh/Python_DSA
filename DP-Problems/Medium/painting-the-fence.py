def countWays(n, k):
    MOD = 1000000007
    
    if n == 1:
        return k % MOD
    
    prev2 = k % MOD
    prev1 = (k * k) % MOD
    
    for i in range(3, n + 1):
        curr = ((prev1 + prev2) * (k - 1)) % MOD
        prev2 = prev1
        prev1 = curr
    
    return prev1 % MOD

# Example usage:
n = 2
k = 100000
print(countWays(n, k))  # Output: 999999937

###################################################################################

def countWays(n, k):
    MOD = 10**9 + 7
    
    # If there's only one post, there are k ways to paint it.
    if n == 1:
        return k
    
    # dp[i] will store the number of ways to paint up to the i-th post
    dp = [0] * (n + 1)
    
    # Base cases
    dp[1] = k
    dp[2] = k * k
    
    # Fill dp array for all posts from 3 to n
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) * (k - 1)
        dp[i] %= MOD
    
    return dp[n]

# Example usage:
n = 3
k = 2
print(countWays(n, k))  # Output: 6

