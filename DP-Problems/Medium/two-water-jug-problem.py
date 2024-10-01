import math

def minSteps(m, n, d):
    # Function to calculate GCD
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    # Function to simulate jug filling process
    def pour(fromJugCapacity, toJugCapacity, d):
        fromJug = toJug = 0  # Initializing both jugs with 0 water
        steps = 0
        
        while fromJug != d and toJug != d:
            # If the from jug is empty, fill it
            if fromJug == 0:
                fromJug = fromJugCapacity
                steps += 1
            
            # If the to jug is full, empty it
            if toJug == toJugCapacity:
                toJug = 0
                steps += 1
            
            # Pour water from the fromJug to the toJug
            transfer = min(fromJug, toJugCapacity - toJug)
            toJug += transfer
            fromJug -= transfer
            steps += 1
            
            # If we have d liters in either jug, return the number of steps
            if fromJug == d or toJug == d:
                return steps
        
        return steps
    
    # If d is greater than the capacity of both jugs, it's impossible
    if d > max(m, n):
        return -1
    
    # If d is not a multiple of the GCD of m and n, it's impossible
    if d % gcd(m, n) != 0:
        return -1
    
    if n == d or m == d:
        return 1
    
    # Get the minimum of the two strategies
    return min(pour(m, n, d), pour(n, m, d))

# Example usage
m = 3
n = 5
d = 4
print(minSteps(m, n, d))  # Output: 6
