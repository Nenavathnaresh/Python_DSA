def maximumPath(n, mat):
    # Create a dp table initialized with the same values as mat
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the first row of dp with the first row of mat
    for c in range(n):
        dp[0][c] = mat[0][c]
    
    # Fill the dp table
    for r in range(1, n):
        for c in range(n):
            # Get the maximum value from the possible previous positions
            best_prev = dp[r-1][c]
            if c > 0:
                best_prev = max(best_prev, dp[r-1][c-1])
            if c < n-1:
                best_prev = max(best_prev, dp[r-1][c+1])
            
            # Update the current dp cell
            dp[r][c] = mat[r][c] + best_prev
    
    # The answer is the maximum value in the last row
    return max(dp[-1])

# Example usage:
n = 2
mat = [[348, 391], [618, 193]]
print(maximumPath(n, mat))  # Output: 1009
