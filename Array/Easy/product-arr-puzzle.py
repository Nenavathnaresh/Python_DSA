def productArray(nums):
    n = len(nums)
    
    if n == 1:
        return [0]  # If there's only one element, the product of all other elements is 0.
    
    # Initialize the left and right arrays
    left = [0] * n
    right = [0] * n
    result = [0] * n
    
    # Build the left array
    left[0] = 1
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    
    # Build the right array
    right[n - 1] = 1
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    
    # Construct the result array
    for i in range(n):
        result[i] = left[i] * right[i]
    
    return result

# Example usage:
nums = [10, 3, 5, 6, 2]
print(productArray(nums))  # Output: [180, 600, 360, 300, 900]

nums = [12, 0]
print(productArray(nums))  # Output: [0, 12]
