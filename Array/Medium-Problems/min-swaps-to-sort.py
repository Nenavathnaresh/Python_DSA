def minSwaps(nums):
    # Create a list of tuples (value, index)
    arr_with_index = [(num, i) for i, num in enumerate(nums)]
    
    # Sort based on the values
    arr_with_index.sort(key=lambda x: x[0])
    
    # Initialize visited array
    visited = [False] * len(nums)
    
    # Initialize swap count
    swaps = 0
    
    # Traverse the array elements
    for i in range(len(nums)):
        # If element is already in the correct place or visited, continue
        if visited[i] or arr_with_index[i][1] == i:
            continue
        
        # Start a cycle
        cycle_size = 0
        j = i
        
        # While we haven't completed the cycle
        while not visited[j]:
            visited[j] = True
            # Move to the next node in the cycle
            j = arr_with_index[j][1]
            cycle_size += 1
        
        # If cycle size is greater than 0, then add (cycle_size - 1) to swaps
        if cycle_size > 0:
            swaps += (cycle_size - 1)
    
    return swaps

# Test cases
nums1 = [2, 8, 5, 4]
nums2 = [10, 19, 6, 3, 5]

print(minSwaps(nums1))  # Output: 1
print(minSwaps(nums2))  # Output: 2


################################ time limit exced ##################

# class Solution:
    
# 	def minSwaps(self, nums):
# 		#Code here
# 		n = len(nums)
# 		count = 0 
# 		def min_index(start):
# 		    ind = min(nums[k] for k in range(start,n))
# 		    return nums.index(ind)
		    
# 		for i in range(len(nums)):
# 		    for j in range(i+1,len(nums)):
# 		        if nums[i] > nums[j]:
# 		            min_ind = min_index(j)
# 		            nums[i], nums[min_ind] = nums[min_ind],nums[i]
# 		            count += 1 
# 		            break
# 	    return count
