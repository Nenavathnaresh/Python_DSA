def longestGoodSequence(arr):
    if not arr:
        return 0
    
    # Initialize the lengths of sequences ending in a peak or a valley
    up = 1
    down = 1

    # Iterate through the array to update the lengths
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            up = down + 1
        elif arr[i] < arr[i - 1]:
            down = up + 1

    # The longest good sequence length is the max of up and down
    return max(up, down)

# Example usage:
print(longestGoodSequence([1, 5, 4]))  # Output: 3
print(longestGoodSequence([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))  # Output: 7
