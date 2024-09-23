def findMinInsertions(S):
    n = len(S)
    # Create a DP table to store the length of LPS
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the DP table for substrings of increasing length
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # The minimum insertions needed to make the string a palindrome
    return n - dp[0][n - 1]

# Example usage:
S1 = "abcd"
print(findMinInsertions(S1))  # Output: 3

S2 = "aba"
print(findMinInsertions(S2))  # Output: 0
