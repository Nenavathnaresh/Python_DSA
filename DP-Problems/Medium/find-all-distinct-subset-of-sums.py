def DistinctSum(nums):
    # Initialize a set with a 0 sum (empty subset)
    distinct_sums = {0}

    # Iterate over each number in the input set
    for num in nums:
        # Generate new sums by adding the current num to all existing sums
        new_sums = set()
        for s in distinct_sums:
            new_sums.add(s + num)
        
        # Add the new sums to the distinct_sums set
        distinct_sums.update(new_sums)
    
    # Return the distinct sums in sorted order
    return sorted(distinct_sums)

# Example usage:
nums1 = [1, 2]
print(DistinctSum(nums1))  # Output: [0, 1, 2, 3]

nums2 = [1, 2, 3]
print(DistinctSum(nums2))  # Output: [0, 1, 2, 3, 4, 5, 6]
