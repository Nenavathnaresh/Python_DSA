def getMinDiff(arr, n, k):
    # Sort the array
    arr.sort()
    
    # Initialize the result with the initial difference between max and min heights
    initial_diff = arr[n-1] - arr[0]
    
    # Initialize the smallest and largest after increasing/decreasing by K
    smallest = arr[0] + k
    largest = arr[n-1] - k
    
    # Initialize the result with the initial difference
    min_diff = initial_diff
    
    # Traverse the sorted array and compute the new minimum difference
    for i in range(n-1):
        min_elem = min(smallest, arr[i+1] - k)
        max_elem = max(largest, arr[i] + k)
        min_diff = min(min_diff, max_elem - min_elem)
    
    return min_diff

# Example usage:
arr1 = [1, 5, 8, 10]
n1 = len(arr1)
k1 = 2
print(getMinDiff(arr1, n1, k1))  # Output: 5

arr2 = [3, 9, 12, 16, 20]
n2 = len(arr2)
k2 = 3
print(getMinDiff(arr2, n2, k2))  # Output: 11
