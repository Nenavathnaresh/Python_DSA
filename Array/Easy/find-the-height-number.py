def findPeakElement(n, a):
    left, right = 0, n - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if a[mid] > a[mid + 1]:
            # Peak must be in the left half including mid
            right = mid
        else:
            # Peak must be in the right half excluding mid
            left = mid + 1
    
    # left should be pointing to the peak element
    return a[left]

# Example usage:

# Example 1:
arr1 = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
n1 = len(arr1)
print(findPeakElement(n1, arr1))  # Output: 6

# Example 2:
arr2 = [1, 2, 3, 4, 5]
n2 = len(arr2)
print(findPeakElement(n2, arr2))  # Output: 5
