
# ====>>> It is similar like playing cards in your hands.
#         the array is vertually split into a sorted and unsorted part , values from the unsorted part
#         are picked and placed in the correct position in the sorted part 


arr = [12, 11, 13, 5, 6]
n = len(arr)

for i in range(1,n):
    key = arr[i]
    j = i-1
    while j>=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1 
    arr[j+1] = key 
print(arr)


# Time complexity = o(N^2)
# Space complexity = o(1)
# Inplace algorithm
# it is stable and applicable for small data that are partially sorted 