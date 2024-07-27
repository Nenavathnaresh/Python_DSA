def min_insertions_to_palindrome(s: str) -> int:
    n = len(s)
    
    # Create a 2D DP table initialized with zeros
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # Build the table. The outer loop is for substring lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
    
    # The result is the minimum insertions needed for the whole string
    return dp[0][n - 1]

# Test cases
print(min_insertions_to_palindrome("abcd"))  # Output: 3
print(min_insertions_to_palindrome("aa"))    # Output: 0
