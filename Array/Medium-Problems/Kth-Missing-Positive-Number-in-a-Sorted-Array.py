def findKthPositive(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    
    # The kth missing number is:
    return low + k

# Example Usage
print(findKthPositive([2, 3, 4, 7, 11], 5))  # Output: 9
print(findKthPositive([1, 2, 3], 2))         # Output: 5
print(findKthPositive([3, 5, 9, 10, 11, 12], 2))  # Output: 2
