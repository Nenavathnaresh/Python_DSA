# from sortedcontainers import SortedList

# def longestPerfectPiece(arr, N):
    
#     start = 0
    
#     window = SortedList()
#     max_length = 0
    
#     for end in range(N):
        
#         window.add(arr[end])
        
       
#         while window[-1] - window[0] > 1:
           
#             window.remove(arr[start])
#             start += 1
        
        
#         max_length = max(max_length, end - start + 1)
    
#     return max_length

# Example usage:
arr1 = [8, 8, 8, 8]
N1 = 4
# print(longestPerfectPiece(arr1, N1))  # Output: 4

arr2 = [5, 4, 5, 5, 6, 7, 8, 8, 8, 7, 6]
N2 = 11
# print(longestPerfectPiece(arr2, N2))  # Output: 5
