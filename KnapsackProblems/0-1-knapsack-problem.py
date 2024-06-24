def knapSack(W, wt, val, n):
    # Initialize a 2D dp array with (n+1) rows and (W+1) columns filled with 0
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the dp array in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                # max value obtained by either including or excluding the current item
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                # If the current item's weight is more than the current capacity
                dp[i][w] = dp[i - 1][w]
    
    # The last cell of dp array will have the maximum value with the given capacity
    return dp[n][W]

# Example usage:
N1 = 3
W1 = 4
values1 = [1, 2, 3]
weights1 = [4, 5, 1]
print(knapSack(W1, weights1, values1, N1))  # Output: 3

N2 = 3
W2 = 3
values2 = [1, 2, 3]
weights2 = [4, 5, 6]
print(knapSack(W2, weights2, values2, N2))  # Output: 0
