def NumberOfPath(A, B):
    # Create a DP table initialized to 0
    dp = [[0 for _ in range(B)] for _ in range(A)]
    
    # Fill the first row with 1, since there's only one way to move right
    for i in range(A):
        dp[i][0] = 1
        
    # Fill the first column with 1, since there's only one way to move down
    for j in range(B):
        dp[0][j] = 1
    
    # Fill the rest of the DP table
    for i in range(1, A):
        for j in range(1, B):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # Return the value at the bottom-right corner
    return dp[A-1][B-1]

# Example usage:
A = 2
B = 2
print(NumberOfPath(A, B))  # Output: 2

A = 3
B = 4
print(NumberOfPath(A, B))  # Output: 10
