def count(N):
    # Initialize an array to store the Catalan numbers
    catalan = [0] * (N // 2 + 1)
    
    # The first Catalan number is 1
    catalan[0] = 1
    
    # Compute the remaining Catalan numbers
    for i in range(1, N // 2 + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    
    # Return the N//2 th Catalan number
    return catalan[N // 2]

# Example usage
print(count(2))  # Output: 1
print(count(4))  # Output: 2
print(count(6))  # Output: 5
