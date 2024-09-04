def maxGold(n, m, M):
    # Create a dp array to store the results of subproblems
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    # Fill the dp table from right to left
    for j in range(m-1, -1, -1):
        for i in range(n):
            # If we go to the cell to the right (right move)
            right = dp[i][j+1] if j < m-1 else 0
            
            # If we go to the cell to the right-up (right-up move)
            right_up = dp[i-1][j+1] if i > 0 and j < m-1 else 0
            
            # If we go to the cell to the right-down (right-down move)
            right_down = dp[i+1][j+1] if i < n-1 and j < m-1 else 0
            
            # Calculate the maximum gold that can be collected from this cell
            dp[i][j] = M[i][j] + max(right, right_up, right_down)
    
    # The result is the maximum value in the first column
    max_gold = max(dp[i][0] for i in range(n))
    return max_gold
