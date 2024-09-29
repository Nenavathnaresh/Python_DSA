def totalParts(arr, k):
    total_parts = 0
    for num in arr:
        # Calculate the number of parts needed for num
        total_parts += (num + k - 1) // k
    return total_parts

# Example usage:
k1 = 3
arr1 = [5, 8, 10, 13]
print(totalParts(arr1, k1))  # Output: 14

k2 = 4
arr2 = [10, 2, 3, 4, 7]
print(totalParts(arr2, k2))  # Output: 8


#########################################################

class Solution:
    def totalCount(self, k, arr):
        # code here
        count = 0
        n = len(arr)
        for i in range(n):
            q = arr[i] // k 
            count += q 
            r = arr[i] % k
            
            if r != 0 :
                count += 1 
        return count 