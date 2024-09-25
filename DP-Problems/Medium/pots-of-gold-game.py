def maxCoins(N, A):
    # dp[i][j] will store the maximum coins X can collect from pots i to j
    dp = [[0] * N for _ in range(N)]
    
    # Fill the dp array for one-pot cases
    for i in range(N):
        dp[i][i] = A[i]
    
    # Fill the dp array for two-pot cases
    for i in range(N - 1):
        dp[i][i + 1] = max(A[i], A[i + 1])
    
    # Fill for larger subproblems
    for length in range(2, N):  # Length of the subarray
        for i in range(N - length):
            j = i + length
            # X chooses the pot at i or j, and Y plays optimally
            pick_i = A[i] + min(dp[i + 2][j] if i + 2 <= j else 0, dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            pick_j = A[j] + min(dp[i + 1][j - 1] if i + 1 <= j - 1 else 0, dp[i][j - 2] if i <= j - 2 else 0)
            dp[i][j] = max(pick_i, pick_j)
    
    # The answer is in dp[0][N-1], meaning the whole array is available
    return dp[0][N-1]

# Example usage:
N = 4
A = [8, 15, 3, 7]
print(maxCoins(N, A))  # Output: 22

N = 4
A = [2, 2, 2, 2]
print(maxCoins(N, A))  # Output: 4
