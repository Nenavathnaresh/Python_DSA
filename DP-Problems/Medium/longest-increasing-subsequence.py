def binary_search(lis, num):
    left, right = 0, len(lis) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lis[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left

def longestSubsequence(n, a):
    lis = []
    
    for num in a:
        # Find the position using our custom binary search function
        pos = binary_search(lis, num)
        
        # If pos is equal to the length of lis, append num
        if pos == len(lis):
            lis.append(num)
        else:
            # Otherwise, replace the element at position pos with num
            lis[pos] = num
    
    # The length of lis is the length of the longest increasing subsequence
    return len(lis)

####################################################################################

