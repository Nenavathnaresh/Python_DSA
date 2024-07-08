def search(self,arr,key):
        # Complete this function
        for i in range(len(arr)):
            if arr[i] == key:
                return i 
        return -1

####################################################################################################

def search_in_rotated_array(arr, key):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        
        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Otherwise, the right half must be sorted
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

# Example usage:
arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key1 = 10
print(search_in_rotated_array(arr1, key1))  # Output: 5

arr2 = [3, 5, 1, 2]
key2 = 6
print(search_in_rotated_array(arr2, key2))  # Output: -1
