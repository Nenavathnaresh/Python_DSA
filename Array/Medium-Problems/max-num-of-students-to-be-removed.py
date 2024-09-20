def binary_search(lis, height):
    # Perform a binary search to find the index where height should be inserted/replaced
    low, high = 0, len(lis) - 1
    while low <= high:
        mid = (low + high) // 2
        if lis[mid] < height:
            low = mid + 1
        else:
            high = mid - 1
    return low

def removeStudents(H, N):
    # Array to store the longest increasing subsequence
    lis = []
    
    for height in H:
        # Find the position to replace or insert the current height using binary search
        pos = binary_search(lis, height)
        
        # If pos is equal to the length of lis, it means we can extend the subsequence
        if pos < len(lis):
            lis[pos] = height
        else:
            lis.append(height)
    
    # The number of students to remove is total students - length of longest increasing subsequence
    return N - len(lis)

# Example usage:
H1 = [9, 1, 2, 3, 1, 5]
N1 = len(H1)
print(removeStudents(H1, N1))  # Output: 2

H2 = [1, 2, 3]
N2 = len(H2)
print(removeStudents(H2, N2))  # Output: 0


##############################################################################################

import bisect

def removeStudents(H, N):
    # Array to store the longest increasing subsequence
    lis = []
    
    for height in H:
        # Find the position to replace or insert the current height
        pos = bisect.bisect_left(lis, height)
        
        # If pos is equal to the length of lis, it means we can extend the subsequence
        if pos < len(lis):
            lis[pos] = height
        else:
            lis.append(height)
    
    # The number of students to remove is total students - length of longest increasing subsequence
    return N - len(lis)

# Example usage:
H1 = [9, 1, 2, 3, 1, 5]
N1 = len(H1)
print(removeStudents(H1, N1))  # Output: 2

H2 = [1, 2, 3]
N2 = len(H2)
print(removeStudents(H2, N2))  # Output: 0
