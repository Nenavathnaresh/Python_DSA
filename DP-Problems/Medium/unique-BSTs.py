MOD = 10**9 + 7

def numTrees(n):
    # dp[i] will store the number of unique BSTs that can be formed with 'i' nodes
    dp = [0] * (n + 1)
    
    # Base case
    dp[0] = 1  # There's one empty tree with 0 nodes
    
    # Fill dp array using the formula
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = (dp[i] + dp[j - 1] * dp[i - j]) % MOD
    
    return dp[n]

# Example usage:
print(numTrees(2))  # Output: 2
print(numTrees(3))  # Output: 5
