def minCost(colors, N):
    # Initialize variables to store the previous costs
    prev_pink = colors[0][0]
    prev_black = colors[0][1]
    prev_yellow = colors[0][2]
    
    # Iterate over the walls starting from the second one
    for i in range(1, N):
        # For current wall i, calculate the minimum cost for each color
        curr_pink = min(prev_black, prev_yellow) + colors[i][0]
        curr_black = min(prev_pink, prev_yellow) + colors[i][1]
        curr_yellow = min(prev_pink, prev_black) + colors[i][2]
        
        # Update the previous costs for the next iteration
        prev_pink, prev_black, prev_yellow = curr_pink, curr_black, curr_yellow
    
    # The answer is the minimum cost of painting the last wall with any color
    return min(prev_pink, prev_black, prev_yellow)

# Example usage
colors1 = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
N1 = 3
print(minCost(colors1, N1))  # Output: 10

colors2 = [[1, 2, 3], [1, 4, 6]]
N2 = 2
print(minCost(colors2, N2))  # Output: 3


#########################################################################################

def minCost(colors, N):
    # Initialize a dp array where dp[i][j] stores the minimum cost to paint
    # the i-th wall with color j (0: pink, 1: black, 2: yellow)
    dp = [[0] * 3 for _ in range(N)]
    
    # Base case: for the first wall, take the costs directly
    dp[0][0] = colors[0][0]  # Cost of painting the first wall pink
    dp[0][1] = colors[0][1]  # Cost of painting the first wall black
    dp[0][2] = colors[0][2]  # Cost of painting the first wall yellow
    
    # Fill the dp array using the state transition formula
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + colors[i][0]  # Current wall painted pink
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + colors[i][1]  # Current wall painted black
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + colors[i][2]  # Current wall painted yellow
    
    # The answer is the minimum cost of painting the last wall with any color
    return min(dp[N-1][0], dp[N-1][1], dp[N-1][2])

# Example usage
colors1 = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
N1 = 3
print(minCost(colors1, N1))  # Output: 10

colors2 = [[1, 2, 3], [1, 4, 6]]
N2 = 2
print(minCost(colors2, N2))  # Output: 3
