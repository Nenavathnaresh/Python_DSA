def find_smallest_missing(arr):
    # Initialize the result to be the smallest possible value, i.e., 1
    res = 1
    
    # Traverse the sorted array
    for num in arr:
        # If the current number is greater than the result, we found the gap
        if num > res:
            break
        # Otherwise, include this number in our subset sums
        res += num
    
    return res

# Example usage:
arr1 = [1, 2, 3]
arr2 = [3, 6, 9, 10, 20, 28]

print(find_smallest_missing(arr1))  # Output: 7
print(find_smallest_missing(arr2))  # Output: 1
