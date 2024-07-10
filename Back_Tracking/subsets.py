def subsets(arr):
    def backtrack(start, path):
        result.append(path[:])  # Append a copy of the current subset (path)
        for i in range(start, len(arr)):
            # Include arr[i] in the subset
            path.append(arr[i])
            # Move on to the next element
            backtrack(i + 1, path)
            # Backtrack, remove arr[i] from the subset
            path.pop()
    
    result = []
    backtrack(0, [])
    arr.sort()  # Sort the array to ensure lexicographical order
    return result

# Example usage:
array1 = [1, 2, 3]
print(subsets(array1))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

array2 = [1, 2]
print(subsets(array2))  # Output: [[], [1], [1, 2], [2]]


##########################################################################################################

def subsets(arr):
    n = len(arr)
    result = []
    arr.sort()  # Sort the input array to ensure lexicographical order

    # There are 2^n possible subsets
    for mask in range(1 << n):  # Loop from 0 to 2^n - 1
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Check if the ith bit is set
                subset.append(arr[i])
        result.append(subset)
    
    # Sorting subsets to ensure lexicographical order
    result.sort()
    return result

# Example usage:
array1 = [1, 2, 3]
print(subsets(array1))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

array2 = [1, 2]
print(subsets(array2))  # Output: [[], [1], [1, 2], [2]]
