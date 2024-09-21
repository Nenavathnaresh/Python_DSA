def maxLength(arr, n):
    # Variables to track the lengths of the longest subarrays
    pos_len = 0  # Longest positive product subarray length
    neg_len = 0  # Longest negative product subarray length
    max_len = 0  # Overall maximum positive product subarray length
    
    for i in range(n):
        if arr[i] > 0:
            # If the current element is positive, increment pos_len
            pos_len += 1
            # If there was a negative subarray, increment neg_len
            if neg_len > 0:
                neg_len += 1
        elif arr[i] < 0:
            # If the current element is negative, swap pos_len and neg_len
            temp = pos_len
            pos_len = neg_len + 1 if neg_len > 0 else 0
            neg_len = temp + 1
        else:
            # If the current element is zero, reset both lengths
            pos_len = 0
            neg_len = 0
        
        # Update the maximum positive subarray length
        max_len = max(max_len, pos_len)
    
    return max_len

# Example usage:
arr1 = [0, 1, -2, -3, -4]
print(maxLength(arr1, len(arr1)))  # Output: 3

arr2 = [-1, -2, 0, 1, 2]
print(maxLength(arr2, len(arr2)))  # Output: 2
