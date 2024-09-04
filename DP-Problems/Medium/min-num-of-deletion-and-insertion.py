def lcs(str1, str2, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def min_operations(str1, str2):
    m, n = len(str1), len(str2)
    lcs_length = lcs(str1, str2, m, n)
    
    deletions = m - lcs_length
    insertions = n - lcs_length
    
    return deletions + insertions

# Example usage:
str1 = "heap"
str2 = "pea"
print(min_operations(str1, str2))  # Output: 3

str1 = "geeksforgeeks"
str2 = "geeks"
print(min_operations(str1, str2))  # Output: 8
