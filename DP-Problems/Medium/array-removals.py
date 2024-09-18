def removals(arr, n, k):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Use a sliding window to find the largest subarray with arr[j] - arr[i] <= k
    i = 0
    max_len = 0  # To store the maximum length of valid subarray
    for j in range(n):
        # While the difference between the current elements is greater than k
        while arr[j] - arr[i] > k:
            i += 1
        # Calculate the length of the current valid subarray
        max_len = max(max_len, j - i + 1)
    
    # Step 3: The minimum removals needed is the total elements minus the largest valid subarray length
    return n - max_len

# Example usage:
arr1 = [1, 3, 4, 9, 10, 11, 12, 17, 20]
n1 = len(arr1)
k1 = 4
print(removals(arr1, n1, k1))  # Output: 5

arr2 = [1, 5, 6, 2, 8]
n2 = len(arr2)
k2 = 2
print(removals(arr2, n2, k2))  # Output: 3
