def nextPermutation(arr):
    n = len(arr)
    # Step 1: Find the pivot point
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i >= 0:  # There is a valid pivot
        # Step 2: Find the next largest element to the right of the pivot
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Step 3: Swap the pivot with this element
        arr[i], arr[j] = arr[j], arr[i]
    
    # Step 4: Reverse the portion to the right of the pivot
    arr[i + 1:] = reversed(arr[i + 1:])

# Example usage:
arr = [2, 4, 1, 7, 5, 0]
nextPermutation(arr)
print(arr)  # Output: [2, 4, 5, 0, 1, 7]

arr = [3, 2, 1]
nextPermutation(arr)
print(arr)  # Output: [1, 2, 3]

arr = [3, 4, 2, 5, 1]
nextPermutation(arr)
print(arr)  # Output: [3, 4, 5, 1, 2]
