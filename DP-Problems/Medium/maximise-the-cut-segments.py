def maximizeTheCuts(n, x, y, z):
    # DP array to store the maximum number of cuts for each length
    dp = [-1] * (n + 1)
    
    # Base case: 0 length requires 0 cuts
    dp[0] = 0
    
    # Fill the dp array
    for i in range(1, n + 1):
        if i >= x and dp[i - x] != -1:
            dp[i] = max(dp[i], dp[i - x] + 1)
        if i >= y and dp[i - y] != -1:
            dp[i] = max(dp[i], dp[i - y] + 1)
        if i >= z and dp[i - z] != -1:
            dp[i] = max(dp[i], dp[i - z] + 1)
    
    # If dp[n] is still -1, it means no segments can be made
    return max(0, dp[n])

# Example usage:
n = 4
x = 2
y = 1
z = 1
print(maximizeTheCuts(n, x, y, z))  # Output: 4

n = 5
x = 5
y = 3
z = 2
print(maximizeTheCuts(n, x, y, z))  # Output: 2
