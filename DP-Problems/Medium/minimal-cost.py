def minCost(arr, k):
    n = len(arr)
    # Initialize the dp array with a large value
    dp = [float('inf')] * n
    dp[0] = 0  # Cost to reach the first stone is 0
    
    # Iterate through all stones
    for i in range(n):
        # Check all possible jumps from i to i+j where 1 <= j <= k
        for j in range(1, k + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + abs(arr[i] - arr[i + j]))
    
    # The answer is the minimum cost to reach the last stone
    return dp[n-1]

# Example usage:
arr1 = [10, 30, 40, 50, 20]
k1 = 3
print(minCost(arr1, k1))  # Output: 30

arr2 = [10, 20, 10]
k2 = 1
print(minCost(arr2, k2))  # Output: 20
