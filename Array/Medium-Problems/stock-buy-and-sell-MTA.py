def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0  # No transactions possible

    profit = 0

    # Traverse the prices array
    for i in range(n - 1):
        # If there's an upward trend, add the difference to profit
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]

    return profit

# Example usage
print(maxProfit([100, 180, 260, 310, 40, 535, 695]))  # Output: 865
print(maxProfit([4, 2, 2, 2, 4]))                    # Output: 2
print(maxProfit([1, 2, 3, 4, 5]))                    # Output: 4
print(maxProfit([5, 4, 3, 2, 1]))                    # Output: 0
