def padovan_sequence(n):
    MOD = 10**9 + 7
    
    # Initial values for P(0), P(1), P(2)
    if n == 0 or n == 1 or n == 2:
        return 1
    
    P0, P1, P2 = 1, 1, 1
    
    for i in range(3, n + 1):
        P_next = (P0 + P1) % MOD
        P0, P1, P2 = P1, P2, P_next
    
    return P2

# Test the function with example inputs
print(padovan_sequence(3))  # Output: 2
print(padovan_sequence(4))  # Output: 2
print(padovan_sequence(5))  # Output: 3
print(padovan_sequence(6))  # Output: 4
print(padovan_sequence(7))  # Output: 5
