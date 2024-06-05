def findSwapValues(a, b, n, m):
    sum_a = sum(a)
    sum_b = sum(b)
    
    # Calculate the difference
    diff = sum_a - sum_b
    
    # If diff is not even, no such pair exists
    if diff % 2 != 0:
        return -1
    
    # Calculate the target value to find in b
    target = diff // 2
    
    # Create a set for array b for O(1) lookups
    set_b = set(b)
    
    # Iterate through array a and check for the required pair
    for x in a:
        y = x - target
        if y in set_b:
            return 1
    
    return -1

# Example usage
n1, m1 = 6, 4
a1 = [4, 1, 2, 1, 1, 2]
b1 = [3, 6, 3, 3]
print(findSwapValues(a1, b1, n1, m1))  # Output: 1

n2, m2 = 4, 4
a2 = [5, 7, 4, 6]
b2 = [1, 2, 3, 8]
print(findSwapValues(a2, b2, n2, m2))  # Output: 1
