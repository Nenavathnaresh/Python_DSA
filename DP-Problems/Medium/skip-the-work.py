def minAmount(N, A):
    if N == 1:
        return A[0]
    
    # Initialize take1 and take2
    take2 = 0  # Represents the cost of two tasks before
    take1 = A[0]  # Represents the cost of the previous task
    
    for i in range(1, N):
        # Current task: either take this task or skip it
        current = min(take1, take2) + A[i]
        
        # Update take2 and take1 for the next iteration
        take2 = take1
        take1 = current
    
    # The minimum time required will be take1
    return min(take1, take2)

# Example usage:
A1 = [10, 20]
N1 = 2
print(minAmount(N1, A1))  # Output: 10

A2 = [10, 5, 7, 10]
N2 = 4
print(minAmount(N2, A2))  # Output: 12
