def longestPalindromicSubsequence(S):
    n = len(S)
    # Create a dp table of size n x n initialized to 0
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the dp table
    for length in range(2, n+1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j-1] + 2  # Include both characters
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])  # Exclude one of the characters
    
    # The longest palindromic subsequence will be in dp[0][n-1]
    return dp[0][n-1]

def minimumNumberOfDeletions(S):
    # Length of longest palindromic subsequence
    lps_length = longestPalindromicSubsequence(S)
    # Minimum deletions required = total length - length of LPS
    return len(S) - lps_length

# Example usage:
S = "aebcbda"
print(minimumNumberOfDeletions(S))  # Output: 2

S = "geeksforgeeks"
print(minimumNumberOfDeletions(S))  # Output: 8
