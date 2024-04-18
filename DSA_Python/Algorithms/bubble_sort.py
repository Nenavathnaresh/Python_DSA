# Bubble is simplest sorting algorithm that works by repeatedly swapping the adjacent elements is they are 
# in wrong order. 
# ===>> Not stable for large data sets.

arr = [7,3,9,12,11]
n = len(arr)
for i in range(n-1):
    swapped = False
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True 
    if(swapped == False):
        break
print(arr)


# Time complexity = o(N^2)
# Space complexity = o(1)
# It is stable sorting algorithm
# Inplace Algorithm