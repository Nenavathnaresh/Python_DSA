def NBitBinary(n):
    def generate(curr, ones, zeroes):
        # Base condition: If the current length is equal to n
        if len(curr) == n:
            result.append(curr)
            return
        
        # Add '1' if possible
        generate(curr + '1', ones + 1, zeroes)
        
        # Add '0' if ones are greater than zeroes
        if ones > zeroes:
            generate(curr + '0', ones, zeroes + 1)
    
    result = []
    generate('', 0, 0)
    return sorted(result, reverse=True)

# Test the function with example inputs
print(NBitBinary(2))  # Output: ['11', '10']
print(NBitBinary(3))  # Output: ['111', '110', '101']
