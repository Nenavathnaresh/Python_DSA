def countWays(arr, m, N):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1  # There's one way to make sum 0
    
    for i in range(1, N + 1):  # For each sum i
        for j in range(m):  # Check for each element in arr
            if i >= arr[j]:
                dp[i] = (dp[i] + dp[i - arr[j]]) % MOD
    
    return dp[N]
