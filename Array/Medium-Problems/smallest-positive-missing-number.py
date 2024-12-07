def findMissingPositive(arr):
    n = len(arr)
    
    # Step 1: Segregate positive and non-positive numbers
    j = 0
    for i in range(n):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    # Now, arr[:j] contains non-positive numbers, and arr[j:] contains positive numbers.
    
    # Step 2: Mark the presence of elements
    for i in range(j, n):
        val = abs(arr[i])
        if val - 1 < n - j and arr[val - 1 + j] > 0:
            arr[val - 1 + j] = -arr[val - 1 + j]
    
    # Step 3: Find the first missing positive number
    for i in range(j, n):
        if arr[i] > 0:
            return i - j + 1
    
    return n - j + 1

# Examples
print(findMissingPositive([2, -3, 4, 1, 1, 7]))  # Output: 3
print(findMissingPositive([5, 3, 2, 5, 1]))  # Output: 4
print(findMissingPositive([-8, 0, -1, -4, -3]))  # Output: 1

###################################################################

def missingNumber(arr):
    n = len(arr)
    
    # Step 1: Place each element in its correct position if possible
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            # Swap arr[i] with the element at its correct position
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
    
    # Step 2: Find the first missing positive number
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1  # Missing positive number
    
    # Step 3: If all numbers are in place, return n + 1
    return n + 1

# Examples
print(missingNumber([2, -3, 4, 1, 1, 7]))  # Output: 3
print(missingNumber([5, 3, 2, 5, 1]))      # Output: 4
print(missingNumber([-8, 0, -1, -4, -3]))  # Output: 1


##################################################

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        i = 0 
        while i < n :
            if 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1] :
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            else:
                i += 1
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1 
        return n+1