def zigzag(arr):
    n = len(arr)
    
    # Traverse all array elements
    for i in range(n - 1):
        if i % 2 == 0:
            # If i is even, arr[i] should be less than arr[i+1]
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            # If i is odd, arr[i] should be greater than arr[i+1]
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr

# Test cases
arr1 = [4, 3, 7, 8, 6, 2, 1]
arr2 = [4, 7, 3, 8, 2]

print(zigzag(arr1)) # Expected: [3 < 7 > 4 < 8 > 2 < 6 > 1]
print(zigzag(arr2)) # Expected: [4 < 7 > 3 < 8 > 2]
