def editDistance(str1: str, str2: str) -> int:
    len1 = len(str1)
    len2 = len(str2)
    
    # Initialize the dp table
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Base cases: edit distances from empty strings
    for i in range(len1 + 1):
        dp[i][0] = i  # Deleting all characters from str1 to get an empty str2
    for j in range(len2 + 1):
        dp[0][j] = j  # Inserting all characters of str2 into an empty str1

    # Fill the dp table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed if characters match
            else:
                insert = dp[i][j - 1]  # Insert operation
                delete = dp[i - 1][j]  # Delete operation
                replace = dp[i - 1][j - 1]  # Replace operation
                dp[i][j] = 1 + min(insert, delete, replace)  # Choose the best option

    # Return the result from the dp table
    return dp[len1][len2]

# Example Usage
str1 = "geek"
str2 = "gesek"
print(editDistance(str1, str2))  # Output: 1

str1 = "gfg"
str2 = "gfg"
print(editDistance(str1, str2))  # Output: 0
