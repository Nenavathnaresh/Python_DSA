def custom_bisect_left(dp, num):
    lo, hi = 0, len(dp)
    while lo < hi:
        mid = (lo + hi) // 2
        if dp[mid] < num:
            lo = mid + 1
        else:
            hi = mid
    return lo

def longestSubsequence(n, a):
    if n == 0:
        return 0
    
    # Initialize the list to store the increasing subsequence
    dp = []
    
    for num in a:
        # Use custom binary search to find the index to replace or extend
        idx = custom_bisect_left(dp, num)
        
        # If idx is equal to the length of dp, it means num is greater than all elements in dp
        if idx == len(dp):
            dp.append(num)
        else:
            # Replace the element at the found index with num
            dp[idx] = num
    
    # The length of dp is the length of the longest increasing subsequence
    return len(dp)

# Example usage
n1 = 6
a1 = [5, 8, 3, 7, 9, 1]
print(longestSubsequence(n1, a1))  # Output: 3

n2 = 16
a2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longestSubsequence(n2, a2))  # Output: 6
