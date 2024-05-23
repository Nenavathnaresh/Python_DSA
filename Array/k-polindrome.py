def kPalindrome(str, n, k):
    # Initialize the DP table
    dp = [[0] * n for _ in range(n)]
    
    # Fill the DP table
    for length in range(2, n+1):  # length from 2 to n
        for i in range(n - length + 1):
            j = i + length - 1
            if str[i] == str[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    
    # Check the number of deletions needed for the whole string
    if dp[0][n-1] <= k:
        return 1
    else:
        return 0

# Example usage:
str1 = "abcdecba"
n1 = 8
k1 = 1
print(kPalindrome(str1, n1, k1))  # Output: 1

str2 = "abcdefcba"
n2 = 9
k2 = 1
print(kPalindrome(str2, n2, k2))  # Output: 0
