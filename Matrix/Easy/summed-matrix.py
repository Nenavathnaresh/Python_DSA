def count_cells_with_value_q(n, q):
    # Calculate the valid range of i
    start = max(1, q - n)
    end = min(n, q - 1)
    
    # If the range is invalid, return 0
    if start > end:
        return 0
    
    # Return the count of valid i values
    return end - start + 1

# Example usage:
n1, q1 = 4, 7
print(count_cells_with_value_q(n1, q1))  # Output: 2

n2, q2 = 5, 4
print(count_cells_with_value_q(n2, q2))  # Output: 3
