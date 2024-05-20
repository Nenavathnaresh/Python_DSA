def PowMod(x, n, M):
    result = 1
    base = x % M  # Take modulo M initially to avoid overflow
    
    while n > 0:
        if n % 2 == 1:  # If n is odd, multiply result by the current base
            result = (result * base) % M
        
        base = (base * base) % M  # Square the base
        n //= 2  # Divide n by 2
    
    return result

# Example usage:
print(PowMod(3, 2, 4))  # Output: 1
print(PowMod(2, 6, 10))  # Output: 4
