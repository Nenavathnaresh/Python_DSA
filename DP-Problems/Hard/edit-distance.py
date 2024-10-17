def editDistance(str1, str2):
    m, n = len(str1), len(str2)
    
    # Create a DP table to store results of subproblems
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    
    # Initialize the base cases
    for i in range(m + 1):
        for j in range(n + 1):
            # If str1 is empty, we need to insert all characters of str2
            if i == 0:
                dp[i][j] = j
            # If str2 is empty, we need to delete all characters of str1
            elif j == 0:
                dp[i][j] = i
            # If last characters are the same, ignore the last char
            # and recur for remaining substrings
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # If last characters are different, consider all possibilities
            # and find the minimum
            else:
                dp[i][j] = 1 + min(dp[i-1][j],      # Delete
                                   dp[i][j-1],      # Insert
                                   dp[i-1][j-1])    # Replace
    
    # The result is in the last cell
    return dp[m][n]

# Example usage
str1 = "geek"
str2 = "gesek"
print(editDistance(str1, str2))  # Output: 1
