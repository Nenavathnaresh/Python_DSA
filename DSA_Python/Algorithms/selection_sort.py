#  ===>> The algorithm repetedly selects the smalllest(or largest) element from the unsorted portion of 
#   the list and swaps it with the first element of the unsorted part .
#  this process is reapeated for the remaining unsorted portion until the entire list is sorted

arr = [64,25,12,22,11]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            min_index = j 
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(arr)

# Time complexity = o(N^2)
# space complexity = o(1)     ===>>for temp ind swapping 
# works well with small database 
# it is not stable algorithm
# it is inplace algorith, as it does not require extra space