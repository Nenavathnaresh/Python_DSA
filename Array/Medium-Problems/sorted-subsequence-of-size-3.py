def find3Numbers(arr, n):
    if n < 3:
        return []
    
    left_min = [0] * n
    right_max = [0] * n
    
    # Fill left_min array
    left_min[0] = arr[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], arr[i])
    
    # Fill right_max array
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])
    
    # Now find the triplet
    for j in range(1, n - 1):
        if left_min[j - 1] < arr[j] < right_max[j + 1]:
            return [left_min[j - 1], arr[j], right_max[j + 1]]
    
    return []

# Example usage:
arr1 = [1, 2, 1, 1, 3]
result1 = find3Numbers(arr1, len(arr1))
print(1 if result1 else 0)  # Output: 1

arr2 = [1, 1, 3]
result2 = find3Numbers(arr2, len(arr2))
print(1 if result2 else 0)  # Output: 0
