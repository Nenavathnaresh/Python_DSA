def catchThieves(arr, n, k):
    # Lists to keep track of positions of policemen and thieves
    policemen = []
    thieves = []

    # Populate the lists with indices of policemen and thieves
    for i in range(n):
        if arr[i] == 'P':
            policemen.append(i)
        elif arr[i] == 'T':
            thieves.append(i)
    
    # Initialize pointers for policemen and thieves
    p = 0
    t = 0
    caught = 0

    # Use two pointers to find the maximum number of thieves that can be caught
    while p < len(policemen) and t < len(thieves):
        if abs(policemen[p] - thieves[t]) <= k:
            # A policeman catches a thief
            caught += 1
            p += 1
            t += 1
        elif policemen[p] < thieves[t]:
            # Move the policeman pointer to the right
            p += 1
        else:
            # Move the thief pointer to the right
            t += 1

    return caught

# Example usage
n1, k1 = 5, 1
arr1 = ['P', 'T', 'T', 'P', 'T']
print(catchThieves(arr1, n1, k1))  # Output: 2

n2, k2 = 6, 2
arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
print(catchThieves(arr2, n2, k2))  # Output: 3
