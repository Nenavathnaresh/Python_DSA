
# ===>>It works by divide an array into smaller subarrays,
#     sorting each subarrays and them merging the sorted
#     subarrays back together to form the final sorted array

def Merge(arr):
    if len(arr) > 1:
        mid = len(arr) //2 
        L = arr[:mid]
        R = arr[mid:]
        Merge(L)
        Merge(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1 
            else:
                arr[k] = R[j]
                j += 1 
            k += 1 
        while i < len(L):
            arr[k] = L[i]
            i += 1 
            k += 1 
        while j < len(R):
            arr[k] = R[j]
            j += 1 
            k += 1 
arr = [7,12,9,11,3]
Merge(arr)
print(arr)

# Time complexity = o(nlog(n))
# space complexity = 0(n)
# useful for sorting large data set 
# used in external sorting and custom sorting 
# stable algorithm 
# guarented worst case performance 
# parallelizable

# Drawbacks:
# space complexity 
# not in space 
# not always optimal for small data sets 

