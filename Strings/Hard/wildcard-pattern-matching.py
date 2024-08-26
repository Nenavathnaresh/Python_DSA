def isMatch(pattern, str):
    m, n = len(pattern), len(str)
    
    # DP table initialization
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: Empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns like `*`, `**`, etc., that can match an empty string
    for i in range(1, m + 1):
        if pattern[i-1] == '*':
            dp[i][0] = dp[i-1][0]
    
    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i-1] == '?' or pattern[i-1] == str[j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif pattern[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
    
    # The answer is whether the entire pattern matches the entire string
    return int(dp[m][n])

# Example usage:
pattern = "ba*a?"
str = "baaabab"
print(isMatch(pattern, str))  # Output: 1

pattern = "a*ab"
str = "baaabab"
print(isMatch(pattern, str))  # Output: 0
