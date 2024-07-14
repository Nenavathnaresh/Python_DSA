def segregate0sAnd1s(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
            left += 1

        # Decrement right index while we see 1 at right
        while arr[right] == 1 and left < right:
            right -= 1

        # If left is smaller than right then there is a 1 at left
        # and a 0 at right. Swap them
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Example usage
arr1 = [0, 0, 1, 1, 0]
segregate0sAnd1s(arr1)
print(arr1)  # Output: [0, 0, 0, 1, 1]

arr2 = [1, 1, 1, 1]
segregate0sAnd1s(arr2)
print(arr2)  # Output: [1, 1, 1, 1]
