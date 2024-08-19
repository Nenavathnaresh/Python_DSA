def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quickselect(arr, low, high, k):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)
        
        # If the partition index is k-1, return the element
        if pi == k - 1:
            return arr[pi]
        
        # If k is less than the partition index, search in the left subarray
        if pi > k - 1:
            return quickselect(arr, low, pi - 1, k)
        
        # If k is greater, search in the right subarray
        return quickselect(arr, pi + 1, high, k)
    
    return arr[low]

def kthSmallest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k)

# Example usage:
arr1 = [7, 10, 4, 3, 20, 15]
k1 = 3
print(kthSmallest(arr1, k1))  # Output: 7

arr2 = [7, 10, 4, 20, 15]
k2 = 4
print(kthSmallest(arr2, k2))  # Output: 15
