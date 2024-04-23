

# %%%%%%%%%%%%%%%%%%%%%%%%%%% Iterative Process %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

n = 10  # Number of terms
print(fibonacci_iterative(n))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Using DP %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def fibonaciOfDP(n):
    if n <= 1:
        return n 
    dp = [0] * (n)
    dp[1] = 1 
    for i in range(2,n):
        dp[i] = dp[i-2] + dp[i-1]
    return dp

print(fibonaciOfDP(10))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%% Recursion Process %%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

def fiboRecursive(n):
    if n < 0 :
        return "incorrect Input"
    if n == 1 :
        return 0 
    if n == 2 :
        return 1 
    else:
        return fiboRecursive(n-1) + fiboRecursive(n-2)
print(fiboRecursive(10))

# **************** Method 2 **************

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = 10  # Number of terms
fib_sequence = [fibonacci_recursive(i) for i in range(n)]
print(fib_sequence)
print(fibonacci_recursive(n))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Using Generator function %%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 10  # Number of terms
fib_sequence = list(fibonacci_generator(n))
print(fib_sequence)

# %%%%%%%%%%%%%%%%%%%%%%%%%%% Using Binets Formula %%%%%%%%%%%%%%%%%%%%%%%%%%%

import math

def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi ** n - (1 - phi) ** n) / math.sqrt(5))

n = 10  # Number of terms
fib_sequence = [fibonacci_binet(i) for i in range(n)]
print(fib_sequence)

