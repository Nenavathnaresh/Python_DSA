def findNth(n):
    result = 0
    base = 1
    
    while n > 0:
        # Get the last digit in base 9
        result += (n % 9) * base
        n //= 9
        base *= 10
    
    return result

# Example usage:
print(findNth(8))  # Output: 8
print(findNth(9))  # Output: 10
print(findNth(18))  # Output: 20
