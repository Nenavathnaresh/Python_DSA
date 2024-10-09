def find_largest_pair_sum(arr):
    if len(arr) < 2:
        return -1  # Edge case: array should have at least 2 elements
    
    # Initialize first and second largest elements
    first = second = float('-inf')
    
    # Traverse the array to find the two largest elements
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    
    # Return the sum of the two largest numbers
    return first + second

# Example usage:
arr1 = [12, 34, 10, 6, 40]
arr2 = [10, 20, 30]

print(find_largest_pair_sum(arr1))  # Output: 74
print(find_largest_pair_sum(arr2))  # Output: 50
