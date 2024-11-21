def rotateArray(arr, d):
    n = len(arr)
    d %= n  # Optimize d
    
    # Helper function to reverse a portion of the array
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse the first d elements
    reverse(arr, 0, d - 1)
    
    # Step 2: Reverse the remaining n-d elements
    reverse(arr, d, n - 1)
    
    # Step 3: Reverse the entire array
    reverse(arr, 0, n - 1)

# Example usage
arr = [1, 2, 3, 4, 5]
rotateArray(arr, 2)
print(arr)  # Output: [3, 4, 5, 1, 2]

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
rotateArray(arr, 3)
print(arr)  # Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]

arr = [7, 3, 9, 1]
rotateArray(arr, 9)
print(arr)  # Output: [3, 9, 1, 7]
