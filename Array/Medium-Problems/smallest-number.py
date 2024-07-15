def smallestNumber(s, d):
    # If the sum s cannot be achieved with d digits, return -1
    if s < 1 or s > 9 * d:
        return -1
    
    # Initialize the result as an array of zeros
    result = [0] * d
    
    # Start by placing the smallest non-zero digit in the most significant position
    s -= 1
    result[0] = 1
    
    # Traverse from the last position to the first position, except the most significant position
    for i in range(d - 1, 0, -1):
        # Get the digit to place at the current position
        if s > 9:
            result[i] = 9
            s -= 9
        else:
            result[i] = s
            s = 0
    
    # Add remaining sum to the most significant position if any
    result[0] += s
    
    # Convert the list of digits to a string
    return ''.join(map(str, result))

# Example usage
print(smallestNumber(9, 2))  # Output: "18"
print(smallestNumber(20, 3)) # Output: "299"
print(smallestNumber(7, 1))  # Output: "7"
print(smallestNumber(10, 2)) # Output: "19"
