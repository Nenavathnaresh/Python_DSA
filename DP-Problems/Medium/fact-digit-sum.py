def FactDigit(N):
    # Precompute the factorials of digits 0 to 9
    factorials = [1] * 10
    for i in range(2, 10):
        factorials[i] = factorials[i-1] * i

    result = []
    
    # Start from the largest digit factorial
    for i in range(9, 0, -1):
        while N >= factorials[i]:
            N -= factorials[i]
            result.append(i)
    
    # Return the result in increasing order of digits
    return sorted(result)

# Example usage
print(FactDigit(40321))  # Output: [1, 8]
print(FactDigit(5040))   # Output: [7]
