def Series(n):
    MOD = 10**9 + 7
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    # Initialize the list to store Fibonacci numbers
    fib = [0, 1]
    
    # Compute Fibonacci numbers up to the nth term
    for i in range(2, n + 1):
        next_fib = (fib[i - 1] + fib[i - 2]) % MOD
        fib.append(next_fib)
    
    return fib

# Example Usage:
n1 = 5
print(Series(n1))  # Output: [0, 1, 1, 2, 3, 5]

n2 = 10
print(Series(n2))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
