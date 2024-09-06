def maxProfit(prices):
    n = len(prices)
    
    if n == 0:
        return 0
    
    # Step 1: Calculate left_profit
    left_profit = [0] * n
    min_price = prices[0]
    
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)
    
    # Step 2: Calculate right_profit
    right_profit = [0] * n
    max_price = prices[-1]
    
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profit[i] = max(right_profit[i + 1], max_price - prices[i])
    
    # Step 3: Find maximum sum of left_profit and right_profit
    max_total_profit = 0
    for i in range(n):
        max_total_profit = max(max_total_profit, left_profit[i] + right_profit[i])
    
    return max_total_profit

# Example usage:
prices1 = [10, 22, 5, 75, 65, 80]
prices2 = [2, 30, 15, 10, 8, 25, 80]

print(maxProfit(prices1))  # Output: 87
print(maxProfit(prices2))  # Output: 100
