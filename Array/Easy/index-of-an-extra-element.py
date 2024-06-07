def findExtraElementIndex(arr1, arr2):
    left, right = 0, len(arr2) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr1[mid] == arr2[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

class Solution:
    def findExtra(self,n,a,b):
        #add code here
        b = set(b)
        for i in range(n):
            if a[i] not in b:
                return i 

# Example usage
n1 = 7
arr1 = [2, 4, 6, 8, 9, 10, 12]
arr2 = [2, 4, 6, 8, 10, 12]
print(findExtraElementIndex(arr1, arr2))  # Output: 4

n2 = 6
arr1 = [3, 5, 7, 8, 11, 13]
arr2 = [3, 5, 7, 11, 13]
print(findExtraElementIndex(arr1, arr2))  # Output: 3
