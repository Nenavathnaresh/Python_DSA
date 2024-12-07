def maxProduct(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Initialize variables
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]
    
    # Traverse the array
    for i in range(1, n):
        num = arr[i]
        
        # If current number is negative, swap max and min product
        if num < 0:
            max_product, min_product = min_product, max_product
        
        # Update max_product and min_product
        max_product = max(num, num * max_product)
        min_product = min(num, num * min_product)
        
        # Update the result
        result = max(result, max_product)
    
    return result

# Example Usage
print(maxProduct([-2, 6, -3, -10, 0, 2]))  # Output: 180
print(maxProduct([-1, -3, -10, 0, 60]))    # Output: 60
print(maxProduct([2, 3, 4]))               # Output: 24
