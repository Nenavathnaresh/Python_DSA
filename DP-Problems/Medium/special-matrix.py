MOD = 10**9 + 7

def FindWays(n, m, blocked_cells):
    # Create a grid of n rows and m columns initialized to 0
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    # Mark the blocked cells
    blocked = set((r-1, c-1) for r, c in blocked_cells)
    
    # If the start or end is blocked, return 0 immediately
    if (0, 0) in blocked or (n-1, m-1) in blocked:
        return 0
    
    # Initialize the first cell (1,1) which is dp[0][0]
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(n):
        for j in range(m):
            # If the cell is blocked, no ways to reach it
            if (i, j) in blocked:
                dp[i][j] = 0
            else:
                # Add ways from the top (i-1, j) if within bounds
                if i > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
                # Add ways from the left (i, j-1) if within bounds
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
    
    # Return the result in the bottom-right corner
    return dp[n-1][m-1]

# Example usage:
print(FindWays(3, 3, [(1, 2), (3, 2)]))  # Output: 1
print(FindWays(5, 5, [(5, 5)]))          # Output: 0
