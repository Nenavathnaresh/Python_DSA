def pushZerosToEnd(arr):
    n = len(arr)
    nonZeroIndex = 0  # Pointer to track position for non-zero elements

    for i in range(n):
        # If the current element is non-zero, move it to `nonZeroIndex`
        if arr[i] != 0:
            arr[nonZeroIndex], arr[i] = arr[i], arr[nonZeroIndex]
            nonZeroIndex += 1

    return arr  # Returning the array for demonstration purposes

# Example usage:
arr1 = [1, 2, 0, 4, 3, 0, 5, 0]
print(pushZerosToEnd(arr1))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

arr2 = [10, 20, 30]
print(pushZerosToEnd(arr2))  # Output: [10, 20, 30]

arr3 = [0, 0]
print(pushZerosToEnd(arr3))  # Output: [0, 0]
