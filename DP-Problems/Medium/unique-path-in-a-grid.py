MOD = 10**9 + 7

def uniquePaths(n, m, grid):
    # If the start or end is blocked, return 0
    if grid[0][0] == 0 or grid[n-1][m-1] == 0:
        return 0
    
    # Create a DP table with the same size as the grid
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    # Initialize the starting point
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                dp[i][j] = 0  # Blocked cell, no paths
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]  # Add ways from the top cell
                if j > 0:
                    dp[i][j] += dp[i][j-1]  # Add ways from the left cell
                dp[i][j] %= MOD  # Apply modulo at each step
    
    return dp[n-1][m-1]  # Return the value at the bottom-right corner
