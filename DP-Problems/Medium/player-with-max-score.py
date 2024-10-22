def is1winner(arr, N):
    # DP table to store the score differences
    dp = [[0] * N for _ in range(N)]
    
    # Base case: when the subarray has only one element
    for i in range(N):
        dp[i][i] = arr[i]
    
    # Fill the DP table for all subarray lengths greater than 1
    for length in range(2, N+1):
        for i in range(N - length + 1):
            j = i + length - 1
            dp[i][j] = max(arr[i] - dp[i+1][j], arr[j] - dp[i][j-1])
    
    # If dp[0][N-1] >= 0, Player 1 wins
    return dp[0][N-1] >= 0
