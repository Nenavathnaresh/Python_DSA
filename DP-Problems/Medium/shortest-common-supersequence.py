def shortestCommonSupersequence(X, Y, m, n):
    # Create a DP table to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Length of the shortest common supersequence
    lcs_length = dp[m][n]
    scs_length = m + n - lcs_length
    
    return scs_length

# Example usage:
X = "abcd"
Y = "xycd"
print(shortestCommonSupersequence(X, Y, len(X), len(Y)))  # Output: 6

X = "efgh"
Y = "jghi"
print(shortestCommonSupersequence(X, Y, len(X), len(Y)))  # Output: 6
