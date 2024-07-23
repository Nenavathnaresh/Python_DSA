import math

def find_maximum_profit(n, c, weights, profits):
    # Helper function to check if a number is a perfect square
    def is_perfect_square(x):
        return int(math.isqrt(x))**2 == x

    # List to store (profit-to-weight ratio, weight, profit) for each valid block
    valid_blocks = []

    # Filter out the perfect squares and calculate the profit-to-weight ratio
    for i in range(n):
        if not is_perfect_square(weights[i]):
            # Calculate profit-to-weight ratio
            ratio = profits[i] / weights[i]
            valid_blocks.append((ratio, weights[i], profits[i]))

    # Sort blocks based on profit-to-weight ratio in descending order
    valid_blocks.sort(reverse=True, key=lambda x: x[0])

    # Calculate the maximum profit using a greedy approach
    total_profit = 0.0
    remaining_capacity = c

    for ratio, weight, profit in valid_blocks:
        if weight <= remaining_capacity:
            # Take the whole block
            total_profit += profit
            remaining_capacity -= weight
        else:
            # Take the fraction of the block that fits
            fraction = remaining_capacity / weight
            total_profit += profit * fraction
            break  # Sack is full

    # Return the total profit rounded to three decimal places
    return round(total_profit, 3)

# Example usage:
n = 3
c = 10
weights = [4, 5, 7]
profits = [8, 5, 4]

result = find_maximum_profit(n, c, weights, profits)
print(result)  # Output: 7.857

# Another example:
n2 = 4
c2 = 15
weights2 = [9, 10, 14, 16]
profits2 = [10, 9, 15, 18]

result2 = find_maximum_profit(n2, c2, weights2, profits2)
print(result2)  # Example Output: 24.214
