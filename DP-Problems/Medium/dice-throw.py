def findWays(m, n, x):
    # Create a DP table where dp[i][j] is the number of ways to get sum j with i dice
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    
    # Base case: One way to get sum 0 with 0 dice (by not rolling any dice)
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):  # Iterate over number of dice
        for j in range(1, x + 1):  # Iterate over all possible sums
            dp[i][j] = 0  # Initialize the current cell
            # Calculate dp[i][j] by summing over previous values based on dice faces
            for f in range(1, m + 1):  # Iterate over all faces of the dice
                if j - f >= 0:
                    dp[i][j] += dp[i - 1][j - f]

    # The answer is in dp[n][x], the number of ways to get sum x with n dice
    return dp[n][x]

# Example usage:
print(findWays(6, 3, 12))  # Output: 25
print(findWays(2, 3, 6))   # Output: 1
