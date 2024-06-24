class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractionalKnapsack(w, items, n):
    # Calculate value-to-weight ratio for each item
    items = sorted(items, key=lambda item: item.value/item.weight, reverse=True)
    
    total_value = 0.0  # Total value accumulated in the knapsack
    for item in items:
        if w == 0:  # If the knapsack is already full
            break
        if item.weight <= w:  # If the item can be taken fully
            w -= item.weight
            total_value += item.value
        else:  # If the item needs to be taken fractionally
            total_value += item.value * (w / item.weight)
            w = 0  # Knapsack is full after taking the fractional item
    
    return total_value

# Example 1
n = 3
w = 50
values = [60, 100, 120]
weights = [10, 20, 30]
items = [Item(values[i], weights[i]) for i in range(n)]
print(f"{fractionalKnapsack(w, items, n):.6f}")  # Expected output: 240.000000

# Example 2
n = 2
w = 50
values = [60, 100]
weights = [10, 20]
items = [Item(values[i], weights[i]) for i in range(n)]
print(f"{fractionalKnapsack(w, items, n):.6f}")  # Expected output: 160.000000
