MOD = int(1e9+7)

def totalWays(n, m, grid):
    # Edge case: If the start or end point is blocked by an obstacle
    if grid[0][0] == 1 or grid[n-1][m-1] == 1:
        return 0
    
    # Initialize dp array with 0s
    dp = [[0] * m for _ in range(n)]
    
    # Starting point
    dp[0][0] = 1

    # Fill the dp array
    for i in range(n):
        for j in range(m):
            # If there's an obstacle at grid[i][j], no way to get here
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                # If we can come from the left, add ways from dp[i][j-1]
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
                # If we can come from above, add ways from dp[i-1][j]
                if i > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
    
    # The number of ways to reach the bottom-right corner
    return dp[n-1][m-1]

# Example usage:
n = 3
m = 3
grid = [[0,0,0],[0,1,0],[0,0,0]]
print(totalWays(n, m, grid))  # Output: 2

n = 2
m = 2
grid = [[0,1],[0,0]]
print(totalWays(n, m, grid))  # Output: 1


#################################################################################

MOD = int(1e9+7)

def totalWays(n, m, grid):
    # Edge case: If the start or end point is blocked by an obstacle
    if grid[0][0] == 1 or grid[n-1][m-1] == 1:
        return 0
    
    # Initialize dp array for a single row (current and previous row)
    prev = [0] * m
    curr = [0] * m
    
    # Starting point
    prev[0] = 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                curr[j] = 0  # Obstacle, no way to get here
            else:
                if j > 0:
                    curr[j] = (curr[j-1] + prev[j]) % MOD
                else:
                    curr[j] = prev[j]  # If it's the first column, only use the previous row
        prev = curr[:]  # Move to the next row
    
    return prev[m-1]

# Example usage:
n = 3
m = 3
grid = [[0,0,0],[0,1,0],[0,0,0]]
print(totalWays(n, m, grid))  # Output: 2
