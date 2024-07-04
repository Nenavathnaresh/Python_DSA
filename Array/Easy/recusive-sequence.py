def sequence(n):
    MOD = 10**9 + 7
    
    result = 0
    current = 1  # this is the current number in the sequence
    
    for i in range(1, n + 1):
        term_product = 1
        for j in range(i):
            term_product *= current
            term_product %= MOD
            current += 1
        result += term_product
        result %= MOD
    
    return result

# Test cases
print(sequence(5))  # Expected output: 365527
print(sequence(7))  # Expected output: 6997165
