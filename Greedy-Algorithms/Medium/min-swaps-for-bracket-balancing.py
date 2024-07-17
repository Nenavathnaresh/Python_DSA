def minimumNumberOfSwaps(S):
    imbalance = 0
    swap_count = 0
    left_brackets = 0
    right_count = 0

    for char in S:
        if char == '[':
            left_brackets += 1
            if imbalance > 0:
                swap_count += imbalance
                imbalance -= 1
        else: 
            right_count += 1 
            
            imbalance = (right_count - left_brackets)

    return swap_count

# Example usage:
print(minimumNumberOfSwaps("[]][]["))  # Output: 2
print(minimumNumberOfSwaps("[][]"))    # Output: 0
