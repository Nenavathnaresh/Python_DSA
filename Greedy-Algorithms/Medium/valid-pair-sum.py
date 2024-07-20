def ValidPair(a, N):
    # Sort the array
    a.sort()
    
    count = 0
    i, j = 0, N - 1
    
    while i < j:
        if a[i] + a[j] > 0:
            # If a[i] + a[j] > 0, all pairs (i, k) with k from i to j-1 will have sums greater than 0
            count += (j - i)
            j -= 1
        else:
            i += 1
    
    return count

# Example usage:
N1 = 3
a1 = [3, -2, 1]
print(ValidPair(a1, N1))  # Output: 2

N2 = 4
a2 = [-1, -1, -1, 0]
print(ValidPair(a2, N2))  # Output: 0
