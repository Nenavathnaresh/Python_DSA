def canSplitArray(arr):
    total_sum = sum(arr)
    
    # If total sum is odd, it cannot be split into two equal parts
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    left_sum = 0
    
    # Traverse the array and keep a running sum
    for num in arr:
        left_sum += num
        
        # If the running sum equals half of the total sum, return True
        if left_sum == target:
            return True
    
    # If we complete the loop without finding the split point, return False
    return False

# Example usage:
arr1 = [1, 2, 3, 4, 5, 5]
arr2 = [4, 3, 2, 1]

print(canSplitArray(arr1))  # Output: True
print(canSplitArray(arr2))  # Output: False

####################################################################################################


class Solution:
    def canSplit(self, arr):
        #code here
        total_sum = sum(arr)
        curr_sum = 0
        for num in arr:
            curr_sum += num 
            total_sum -= num 
            if curr_sum == total_sum :
                return True 
        return False