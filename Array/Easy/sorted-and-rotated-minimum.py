def findMin(arr):
    low, high = 0, len(arr) - 1
    
    while low < high:
        mid = low + (high - low) // 2

        # If mid element is greater than the last element, the min is in the right half
        if arr[mid] > arr[high]:
            low = mid + 1
        elif arr[mid] < arr[high]:
            # The min is in the left half, including mid
            high = mid
        else:
            # Handle duplicates: decrement the high pointer
            high -= 1
    
    return arr[low]

# Example Usage
print(findMin([5, 6, 1, 2, 3, 4]))  # Output: 1
print(findMin([3, 2, 2, 2]))        # Output: 2
print(findMin([4, 4, 4]))           # Output: 4


###################################


class Solution:
    def findMin(self, arr):
        #complete the function here
        # return min(arr)
        mini = float("inf")
        for num in arr:
            if num < mini:
                mini = num
        return mini