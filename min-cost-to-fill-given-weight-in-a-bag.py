def minimumCost(n, w, cost):
    # Initialize dp array with infinity
    dp = [float('inf')] * (w + 1)
    
    # Base case: cost to buy 0 kg of oranges is 0
    dp[0] = 0
    
    # Fill dp array
    for i in range(1, n + 1):
        if cost[i - 1] != -1:  # only consider valid packets
            for j in range(i, w + 1):
                if dp[j - i] != float('inf'):
                    dp[j] = min(dp[j], dp[j - i] + cost[i - 1])
    
    # If dp[w] is still infinity, it means we cannot make exactly w kg
    return dp[w] if dp[w] != float('inf') else -1

# Example usage:
n = 5
cost = [20, 10, 4, 50, 100]
w = 5
print(minimumCost(n, w, cost))  # Output: 14

n = 5
cost = [-1, -1, 4, 3, -1]
w = 5
print(minimumCost(n, w, cost))  # Output: -1
