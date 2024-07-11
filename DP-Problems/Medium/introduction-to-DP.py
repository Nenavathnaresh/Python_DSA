MOD = 10**9 + 7

def topDown(n):
    memo = [-1] * (n + 1)
    
    def fib(n):
        if n <= 1:
            return n
        if memo[n] != -1:
            return memo[n]
        memo[n] = (fib(n - 1) + fib(n - 2)) % MOD
        return memo[n]
    
    return fib(n)

# Example usage
print(topDown(5))  # Output: 5
print(topDown(6))  # Output: 8


MOD = 10**9 + 7

def bottomUp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    return dp[n]

# Example usage
print(bottomUp(5))  # Output: 5
print(bottomUp(6))  # Output: 8
