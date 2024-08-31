MOD = 10**9 + 7

def countPs(str):
    n = len(str)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # Base case: Single character palindromes
    for i in range(n):
        dp[i][i] = 1
    
    # Filling the DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if str[i] == str[j]:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] + 1) % MOD
            else:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
    
    # Return the answer for the whole string
    return dp[0][n - 1]

# Example usage:
str1 = "abcd"
print(countPs(str1))  # Output: 4

str2 = "aab"
print(countPs(str2))  # Output: 4
