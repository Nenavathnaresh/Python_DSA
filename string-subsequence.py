MOD = int(1e9+7)

def countWays(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Create the dp table
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize base case
    for i in range(n + 1):
        dp[i][0] = 1  # An empty s2 is a subsequence of any prefix of s1
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
            else:
                dp[i][j] = dp[i - 1][j] % MOD
    
    return dp[n][m]

# Example usage:
s1 = "geeksforgeeks"
s2 = "gks"
print(countWays(s1, s2))  # Output: 4

s1 = "problemoftheday"
s2 = "geek"
print(countWays(s1, s2))  # Output: 0
