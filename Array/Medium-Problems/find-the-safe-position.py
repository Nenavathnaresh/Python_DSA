def safePos(n, k):
    result = 0  # Base case: when there's only one person, the safe position is 0 (zero-indexed)
    for i in range(2, n + 1):
        result = (result + k) % i
    return result + 1  # Convert zero-indexed result to one-indexed

# Example usage:
n = 4
k = 2
print(safePos(n, k))  # Output: 1
