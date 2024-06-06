def findFloor(arr, N, x):
    left, right = 0, N - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example 1
N = 7
x = 0
arr = [1, 2, 8, 10, 11, 12, 19]
print(findFloor(arr, N, x))  # Output: -1

# Example 2
N = 7
x = 5
arr = [1, 2, 8, 10, 11, 12, 19]
print(findFloor(arr, N, x))  # Output: 1
