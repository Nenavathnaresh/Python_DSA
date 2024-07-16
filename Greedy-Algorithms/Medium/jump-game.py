def canReach(N, A):
    max_reach = 0  # Initialize the farthest index we can reach
    
    for i in range(N):
        if i > max_reach:
            # If current index is greater than the farthest index we can reach
            return 0
        max_reach = max(max_reach, i + A[i])  # Update the farthest index we can reach
        if max_reach >= N - 1:
            # If we can reach or exceed the last index
            return 1
    
    return 0

# Example usage:
N1 = 6
A1 = [1, 2, 0, 3, 0, 0]
print(canReach(N1, A1))  # Output: 1

N2 = 3
A2 = [1, 0, 2]
print(canReach(N2, A2))  # Output: 0
