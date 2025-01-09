def subarraySum(arr, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}  # To handle cases where prefix_sum == k
    
    for num in arr:
        prefix_sum += num
        
        # Check if prefix_sum - k exists in the map
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        
        # Add current prefix_sum to the map
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum] += 1
        else:
            prefix_map[prefix_sum] = 1
    
    return count

# Example usage:
arr1 = [10, 2, -2, -20, 10]
k1 = -10
print(subarraySum(arr1, k1))  # Output: 3

arr2 = [9, 4, 20, 3, 10, 5]
k2 = 33
print(subarraySum(arr2, k2))  # Output: 2

arr3 = [1, 3, 5]
k3 = 0
print(subarraySum(arr3, k3))  # Output: 0
