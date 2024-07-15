class Pair:
    def __init__(self, a, b):
        self.first = a
        self.second = b

def maxChainLen(P, N):
    # Sort the pairs based on the second element of each pair
    P.sort(key=lambda x: x.second)
    
    # Initialize the end of the last selected pair and the count of the maximum chain length
    last_end = float('-inf')
    max_length = 0
    
    # Iterate through the sorted pairs
    for pair in P:
        # If the current pair can be chained to the last selected pair
        if pair.first > last_end:
            # Select this pair
            last_end = pair.second
            max_length += 1
    
    return max_length

# Example usage:
N1 = 5
P1 = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
print(maxChainLen(P1, N1))  # Output: 3

N2 = 2
P2 = [Pair(5, 10), Pair(1, 11)]
print(maxChainLen(P2, N2))  # Output: 1
