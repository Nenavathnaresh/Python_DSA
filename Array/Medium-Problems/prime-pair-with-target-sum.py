def find_prime_pair(n):
    # Helper function to perform Sieve of Eratosthenes
    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = []
        for p in range(n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes, is_prime
    
    primes, is_prime = sieve(n)
    
    for a in primes:
        b = n - a
        if b >= 2 and is_prime[b]:
            return [a, b]
    
    return [-1, -1]

# Test cases
print(find_prime_pair(10))  # Output: [3, 7]
print(find_prime_pair(3))   # Output: [-1, -1]
print(find_prime_pair(4))   # Output: [2, 2]


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&  

def is_prime_basic(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_pair(n):
    if n < 4:
        return [-1, -1]  # The smallest sum of two primes is 2 + 2 = 4

    for a in range(2, n):
        b = n - a
        if is_prime_basic(a) and is_prime_basic(b) and a <= b:
            return [a, b]
    
    return [-1, -1]

# Example usage:
print(find_prime_pair(10))  # Output: [3, 7]
print(find_prime_pair(3))   # Output: [-1, -1]
print(find_prime_pair(28))  # Output: [5, 23]
print(find_prime_pair(100)) # Output: [3, 97]

