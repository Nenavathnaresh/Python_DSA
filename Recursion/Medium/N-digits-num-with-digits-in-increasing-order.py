def increasingNumbers(n):
    def generate_numbers(current, start, n):
        if n == 0:
            result.append(current)
            return
        for digit in range(start, 10):
            generate_numbers(current * 10 + digit, digit + 1, n - 1)

    result = []
    if n == 1:
        result.append(0)
    for digit in range(1, 10):
        generate_numbers(digit, digit + 1, n - 1)
    
    return result

# Example usage
print(increasingNumbers(1))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(increasingNumbers(2))  # Output: [12, 13, 14, 15, 16, 17, 18, 19, 23, ..., 89]
