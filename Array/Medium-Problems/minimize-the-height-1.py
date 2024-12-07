def getMinDiff(arr, k):
    n = len(arr)
    if n == 1:
        return 0  # Only one tower, no difference

    # Sort the array
    arr.sort()

    # Initial difference between max and min heights
    initial_diff = arr[-1] - arr[0]

    # Initialize the result to the initial difference
    result = initial_diff

    # Traverse the array and find the minimum difference
    for i in range(n - 1):
        # Find the new min and max after modification
        new_min = min(arr[0] + k, arr[i + 1] - k)
        new_max = max(arr[-1] - k, arr[i] + k)
        
        # Update the result
        result = min(result, new_max - new_min)

    return result

# Example usage:
print(getMinDiff([1, 5, 8, 10], 2))  # Output: 5
print(getMinDiff([3, 9, 12, 16, 20], 3))  # Output: 11
