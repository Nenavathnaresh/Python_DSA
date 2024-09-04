def longestBitonicSubsequence(nums):
    n = len(nums)
    
    if n == 0:
        return 0
    
    # Initialize LIS array
    lis = [1] * n
    
    # Compute LIS values from left to right
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Initialize LDS array
    lds = [1] * n
    
    # Compute LDS values from right to left
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    
    # Find the maximum length of bitonic subsequence
    max_len = 0
    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:  # Ensure it's bitonic (both increasing and decreasing)
            max_len = max(max_len, lis[i] + lds[i] - 1)
    
    return max_len

# Example usage:
print(longestBitonicSubsequence([1, 2, 5, 3, 2]))  # Output: 5
print(longestBitonicSubsequence([1, 11, 2, 10, 4, 5, 2, 1]))  # Output: 6
print(longestBitonicSubsequence([10, 20, 30]))  # Output: 0
print(longestBitonicSubsequence([10, 10, 10]))  # Output: 0
