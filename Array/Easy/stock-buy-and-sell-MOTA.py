def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum price encountered so far
        min_price = min(min_price, price)
        # Calculate the profit if the stock is sold at the current price
        profit = price - min_price
        # Update the maximum profit
        max_profit = max(max_profit, profit)
    
    return max_profit
    