def eggDrop(N, K):
    # Initialize a DP table
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    
    # Base cases
    for i in range(1, N + 1):
        dp[i][1] = 1  # 1 floor requires 1 drop
        dp[i][0] = 0  # 0 floors require 0 drops
        
    for j in range(1, K + 1):
        dp[1][j] = j  # With 1 egg, need j drops for j floors
    
    # Fill the DP table
    for i in range(2, N + 1):
        for j in range(2, K + 1):
            dp[i][j] = float('inf')
            for x in range(1, j + 1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(dp[i][j], res)
    
    return dp[N][K]

# Example usage:
N1, K1 = 1, 2
print(eggDrop(N1, K1))  # Output: 2

N2, K2 = 2, 10
print(eggDrop(N2, K2))  # Output: 4
