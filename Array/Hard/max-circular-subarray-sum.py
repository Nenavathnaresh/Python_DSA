def maxSubarraySumCircular(arr):
    # Helper function to find maximum or minimum subarray sum using Kadane's algorithm
    def kadane(nums):
        max_ending_here = max_so_far = nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Total sum of the array
    total_sum = sum(arr)
    
    # Case 1: Maximum subarray sum without wrapping
    max_kadane = kadane(arr)
    
    # Case 2: Minimum subarray sum
    min_kadane = kadane([-x for x in arr])  # Invert signs to find minimum sum
    min_kadane = -min_kadane  # Revert the sign
    
    # Handle the case where all elements are negative
    if max_kadane < 0:
        return max_kadane
    
    # Maximum circular sum
    circular_sum = total_sum - min_kadane
    
    # Return the maximum of the two cases
    return max(max_kadane, circular_sum)

# Examples
print(maxSubarraySumCircular([8, -8, 9, -9, 10, -11, 12]))  # Output: 22
print(maxSubarraySumCircular([10, -3, -4, 7, 6, 5, -4, -1]))  # Output: 23
print(maxSubarraySumCircular([-1, 40, -14, 7, 6, 5, -4, -1]))  # Output: 52
