def MinCoin(arr, amount):
    # Initialize dp array with "infinity"
    dp = [float('inf')] * (amount + 1)
    # Base case: to make amount 0, we need 0 coins
    dp[0] = 0
    
    # Update the dp array
    for coin in arr:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # If dp[amount] is still infinity, it means it's not possible to form that amount
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
arr1 = [1, 2, 5]
amount1 = 11
print(MinCoin(arr1, amount1))  # Output: 3

arr2 = [2, 6]
amount2 = 7
print(MinCoin(arr2, amount2))  # Output: -1
