def longest_common_substring(str1, str2):
    n = len(str1)
    m = len(str2)
    
    # Initialize DP table with 0s
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    max_length = 0  # To keep track of the maximum length of common substring found
    
    # Build the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
    
    return max_length

# Example usage
str1 = "ABCDGH"
str2 = "ACDGHR"
print(longest_common_substring(str1, str2))  # Output: 4

str1 = "ABC"
str2 = "ACB"
print(longest_common_substring(str1, str2))  # Output: 1
