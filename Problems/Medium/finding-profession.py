def profession(level, pos):
    count = 0
    
    # Counting the number of 1s in the binary representation of pos-1
    pos -= 1
    while pos > 0:
        # Check if the least significant bit is 1
        if pos & 1:
            count += 1
        # Right shift pos to process the next bit
        pos >>= 1
    
    # If count of 1s is even, return 'e' (Engineer)
    # If count of 1s is odd, return 'd' (Doctor)
    if count % 2 == 0:
        return 'e'
    else:
        return 'd'

# Example usage
print(profession(4, 2))  # Output: 'd' (Doctor)
print(profession(3, 4))  # Output: 'e' (Engineer)


##################################################################################################

def profession(level, pos):
    # Counting the number of 1s in the binary representation of pos-1
    # We use pos-1 to convert from 1-based to 0-based
    count = bin(pos - 1).count('1')
    
    # If count of 1s is even, return 'e' (Engineer)
    # If count of 1s is odd, return 'd' (Doctor)
    if count % 2 == 0:
        return 'e'
    else:
        return 'd'

# Example usage
print(profession(4, 2))  # Output: 'd' (Doctor)
print(profession(3, 4))  # Output: 'e' (Engineer)
