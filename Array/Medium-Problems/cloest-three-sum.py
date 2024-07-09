def three_sum_closest(arr, target):
    # Sort the array
    arr.sort()
    
    # Initialize the closest sum with a large value
    closest_sum = float('inf')
    
    # Iterate through the array
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            # If the current sum is exactly the target, return it
            if current_sum == target:
                return current_sum
            
            # Update the closest_sum if the current sum is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target) or \
               (abs(current_sum - target) == abs(closest_sum - target) and current_sum > closest_sum):
                closest_sum = current_sum
            
            # Move the pointers based on the comparison of current_sum and target
            if current_sum < target:
                left += 1
            else:
                right -= 1
    
    return closest_sum

# Example usage
print(three_sum_closest([-7, 9, 8, 3, 1, 1], 2))  # Output: 2
print(three_sum_closest([5, 2, 7, 5], 13))        # Output: 14
