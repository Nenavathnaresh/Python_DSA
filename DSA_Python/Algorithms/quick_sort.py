# ===>>Quick sort is a algorithm based on the divide and conquer algorithm that pics an element as a pivot 
# and partions the given array around the picked pivot by placing the picot in its correct position in the 
# sorted array

# 1.Select the pivot element
# 2.Find out the correct position of pivot element in the list by rearranging it 
# 3.Divide the list based on the pivot element 
# 4.Sort the sublist recursively.

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&& first element as Pivot &&&&&&&&&&&&&&&&&&&&&&&&&&&&

def pivotPlace(arr, first, last):
    pivot = arr[first]
    left = first + 1 
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1 
        while left <= right and arr[right] >= pivot:
            right -= 1 
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[first], arr[right] = arr[right], arr[first]
    return right 
def quickSort(arr,first,last):
    if first < last:
        p = pivotPlace(arr, first, last)
        quickSort(arr, first, p-1)
        quickSort(arr, p+1, last)
arr = [10,7,8,9,1,5]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& last element as Pivot &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def pivot(arr, first, last):
    pivot = arr[last]
    left = first
    right = last - 1 
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1 
        while left <= right and arr[right] >= pivot:
            right -= 1 
        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[last], arr[left] = arr[left], arr[last]
    return left 
def quick(arr, first, last):
    if first < last:
        p = pivot(arr, first, last)
        quick(arr, first, p-1)
        quick(arr,p+1, last)
arr = [10,7,8,9,1,5]
n = len(arr)
quick(arr, 0, n-1)
print(arr)