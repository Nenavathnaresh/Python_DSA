def findMinCost(x, y, costX, costY):
    m, n = len(x), len(y)
    
    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the table for base cases
    for i in range(1, m + 1):
        dp[i][0] = i * costX  # Cost of deleting all characters from x up to i
    for j in range(1, n + 1):
        dp[0][j] = j * costY  # Cost of deleting all characters from y up to j
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + costX, dp[i][j - 1] + costY)
    
    # The answer is the minimum cost to make the entire strings identical
    return dp[m][n]

# Example usage:
x = "abcd"
y = "acdb"
costX = 10
costY = 20
print(findMinCost(x, y, costX, costY))  # Output: 30

x = "ef"
y = "gh"
costX = 10
costY = 20
print(findMinCost(x, y, costX, costY))  # Output: 60
