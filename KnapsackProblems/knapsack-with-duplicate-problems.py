def knapSack(N, W, val, wt):
    # Initialize dp array of size W+1 with zeros
    dp = [0] * (W + 1)
    
    # Fill the dp array
    for w in range(1, W + 1):
        for i in range(N):
            if wt[i] <= w:
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
    
    # The answer will be in dp[W]
    return dp[W]

# Example usage:
N = 2
W = 3
val = [1, 1]
wt = [2, 1]
print(knapSack(N, W, val, wt))  # Output: 3

N = 4
W = 8
val = [6, 1, 7, 7]
wt = [1, 3, 4, 5]
print(knapSack(N, W, val, wt))  # Output: 48
