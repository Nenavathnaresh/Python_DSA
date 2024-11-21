def reverseArray(arr):
    start = 0
    end = len(arr) - 1

    # Swap elements using the two-pointer approach
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr  # Return the reversed array for demonstration purposes

# Example Usage:
arr1 = [1, 4, 3, 2, 6, 5]
print(reverseArray(arr1))  # Output: [5, 6, 2, 3, 4, 1]

arr2 = [4, 5, 2]
print(reverseArray(arr2))  # Output: [2, 5, 4]

arr3 = [1]
print(reverseArray(arr3))  # Output: [1]
