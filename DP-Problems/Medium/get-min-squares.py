import math

def minSquares(n):
    # Create a dp array to store the minimum number of squares for each number from 0 to n
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: No number is needed to sum up to zero

    # Compute the minimum squares for each number from 1 to n
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], 1 + dp[i - j * j])
            j += 1

    return dp[n]
