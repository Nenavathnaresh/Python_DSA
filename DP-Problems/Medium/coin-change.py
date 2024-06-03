def count(coins, N, sum):
    # Initialize the dp array with zeros
    dp = [0] * (sum + 1)
    
    # There is one way to make the sum 0, which is to choose nothing
    dp[0] = 1
    
    # Iterate over each coin
    for coin in coins:
        # Update dp array for all sums that can include this coin
        for j in range(coin, sum + 1):
            dp[j] += dp[j - coin]
    
    # The last element of dp array will hold the answer
    return dp[sum]

# Example usage
print(count([1, 2, 3], 3, 4))  # Output: 4
print(count([2, 5, 3, 6], 4, 10))  # Output: 5
