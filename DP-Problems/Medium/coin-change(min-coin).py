def minCoins(coins, m, target_sum):
    # Create a dp array with size of target_sum + 1 and initialize with infinity
    dp = [float('inf')] * (target_sum + 1)
    
    # Base case: Minimum coins needed to make sum 0 is 0
    dp[0] = 0
    
    # Fill dp array
    for coin in coins:
        for j in range(coin, target_sum + 1):
            if dp[j - coin] != float('inf'):
                dp[j] = min(dp[j], dp[j - coin] + 1)
    
    # If dp[target_sum] is still infinity, return -1
    return dp[target_sum] if dp[target_sum] != float('inf') else -1

# Example usage:
coins = [25, 10, 5]
sum_value = 30
print(minCoins(coins, len(coins), sum_value))  # Output: 2

coins = [9, 6, 5, 1]
sum_value = 19
print(minCoins(coins, len(coins), sum_value))  # Output: 3

coins = [5, 1]
sum_value = 0
print(minCoins(coins, len(coins), sum_value))  # Output: 0

coins = [4, 6, 2]
sum_value = 5
print(minCoins(coins, len(coins), sum_value))  # Output: -1
