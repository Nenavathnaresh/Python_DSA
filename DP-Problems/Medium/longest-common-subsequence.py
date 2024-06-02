def lcs(n, m, str1, str2):
    # Create a 2D array to store the lengths of LCS
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Build the dp array from bottom up
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the LCS is in the bottom-right cell of the matrix
    return dp[n][m]

# Example usage:
n1, m1 = 6, 6
str1_1, str2_1 = "ABCDGH", "AEDFHR"
print(lcs(n1, m1, str1_1, str2_1))  # Output: 3

n2, m2 = 3, 2
str1_2, str2_2 = "ABC", "AC"
print(lcs(n2, m2, str1_2, str2_2))  # Output: 2

n3, m3 = 4, 4
str1_3, str2_3 = "XYZW", "XYWZ"
print(lcs(n3, m3, str1_3, str2_3))  # Output: 3
