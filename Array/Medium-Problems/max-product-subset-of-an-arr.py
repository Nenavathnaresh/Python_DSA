def maxProductSubset(arr):
    MOD = 10**9 + 7
    n = len(arr)
    
    if n == 1:
        return arr[0] % MOD
    
    max_negative = float('-inf')
    product = 1
    count_negatives = 0
    count_zeros = 0
    contains_positive = False
    
    for num in arr:
        if num == 0:
            count_zeros += 1
            continue
        
        if num < 0:
            count_negatives += 1
            max_negative = max(max_negative, num)
        
        if num > 0:
            contains_positive = True
        
        product = (product * num) % MOD
    
    # If all elements are zero
    if count_zeros == n:
        return 0
    
    # If there are no positives and an odd number of negatives
    if count_negatives % 2 != 0:
        if count_negatives == 1 and count_zeros + count_negatives == n:
            return 0
        product = (product * pow(max_negative, MOD-2, MOD)) % MOD  # Remove the largest negative number by dividing
    
    return product

# Example usage:
arr1 = [-1, 0, -2, 4, 3]
print(maxProductSubset(arr1))  # Output: 24

arr2 = [-1, 0]
print(maxProductSubset(arr2))  # Output: 0

arr3 = [5]
print(maxProductSubset(arr3))  # Output: 5
