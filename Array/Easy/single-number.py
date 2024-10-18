def findOddOccurrence(arr):
    result = 0
    
    # XOR all elements in the array
    for num in arr:
        result ^= num
    
    # The result will be the number with odd occurrence
    return result

# Example usage
arr1 = [1, 1, 2, 2, 2]
print(findOddOccurrence(arr1))  # Output: 2

arr2 = [8, 8, 7, 7, 6, 6, 1]
print(findOddOccurrence(arr2))  # Output: 1


#######################################################################################

class Solution:
    
    def getSingle(self,arr):
        # code here
        freq = {}
        
        for num in arr:
            if num in freq:
                freq[num] += 1 
            else:
                freq[num] = 1 
        for k,v in freq.items():
            if v % 2 != 0:
                return k
