def findProb(N, x, y, K):
    # Directions for the Knight's movement
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                  (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    # Create a 3D DP array initialized with 0
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K + 1)]
    
    # Base case: Probability of being at (x, y) with 0 moves is 1
    dp[0][x][y] = 1
    
    # Loop through each step from 1 to K
    for k in range(1, K + 1):
        # Loop through each cell on the board
        for i in range(N):
            for j in range(N):
                # Calculate dp[k][i][j] by checking all previous valid positions
                for dx, dy in directions:
                    prev_i = i + dx
                    prev_j = j + dy
                    if 0 <= prev_i < N and 0 <= prev_j < N:
                        dp[k][i][j] += dp[k - 1][prev_i][prev_j] / 8.0
    
    # Sum up the probabilities of all positions after K moves
    result = 0
    for i in range(N):
        for j in range(N):
            result += dp[K][i][j]
    
    return result

# Example usage:
N = 8
x = 0
y = 0
K = 3
print(findProb(N, x, y, K))  # Output: 0.125000

N = 4
x = 1
y = 2
K = 4
print(findProb(N, x, y, K))  # Output: 0.024414
