from collections import Counter

def sortByFrequency(arr):
    # Count the frequency of each element
    freq_map = Counter(arr)
    
    # Sort the array by frequency first (in descending order), then by element value (in ascending order)
    sorted_arr = sorted(arr, key=lambda x: (-freq_map[x], x))
    
    return sorted_arr

# Example usage:
arr1 = [5, 5, 4, 6, 4]
arr2 = [9, 9, 9, 2, 5]
print(sortByFrequency(arr1))  # Output: [4, 4, 5, 5, 6]
print(sortByFrequency(arr2))  # Output: [9, 9, 9, 2, 5]


################################################################################

class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        #code here
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1 
            else:
                freq[num] = 1 
        
        sorted_arr = sorted(arr,key=lambda x : (-freq[x],x))
        
        return sorted_arr