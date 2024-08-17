def isPossible(paths):
    n = len(paths)
    
    # Check if all vertices have an even degree
    for i in range(n):
        degree = sum(paths[i])
        if degree % 2 != 0:
            return 0  # If any vertex has an odd degree, return 0
    
    # If all vertices have even degree, return 1
    return 1

# Example usage:
paths = [
    [0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0]
]
print(isPossible(paths))  # Output: 1

paths = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]
print(isPossible(paths))  # Output: 0
