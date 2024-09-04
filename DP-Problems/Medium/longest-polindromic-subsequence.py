def longestPalinSubseq(S):
    n = len(S)
    # Create a 2D DP array
    dp = [[0] * n for _ in range(n)]
    
    # Single character substrings are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the DP table
    # Length of the substring
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    # The result is in the top-right corner of the DP table
    return dp[0][n-1]
    