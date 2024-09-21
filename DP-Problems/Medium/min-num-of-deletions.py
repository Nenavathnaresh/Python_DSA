def minDeletions(s, n):
    # Create a reverse of the string
    rev_s = s[::-1]
    
    # Initialize a 2D DP array
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill the dp table by finding LCS of s and rev_s
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev_s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # LCS of s and rev_s
    longest_palindromic_subseq = dp[n][n]
    
    # The minimum number of deletions needed
    return n - longest_palindromic_subseq

# Example usage:
n = 7
s = "aebcbda"
print(minDeletions(s, n))  # Output: 2

n = 3
s = "aba"
print(minDeletions(s, n))  # Output: 0

##################################################################################################

def minDeletions(s, n):
    # Create a 2D dp array
    dp = [[0] * n for _ in range(n)]
    
    # Base case: a single character is always a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the DP table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    # The length of the longest palindromic subsequence
    longest_palindromic_subseq = dp[0][n-1]
    
    # The minimum number of deletions needed
    return n - longest_palindromic_subseq

# Example usage:
n = 7
s = "aebcbda"
print(minDeletions(s, n))  # Output: 2

n = 3
s = "aba"
print(minDeletions(s, n))  # Output: 0
