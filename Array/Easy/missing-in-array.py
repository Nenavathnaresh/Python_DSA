def findMissingElement(n, arr):
    # Calculate the expected sum of numbers from 1 to n
    total_sum = n * (n + 1) // 2
    
    # Calculate the sum of the elements in the array
    arr_sum = sum(arr)
    
    # The missing number is the difference
    return total_sum - arr_sum

# Example usage:
n = 5
arr = [1, 2, 3, 5]
print(findMissingElement(n, arr))  # Output: 4

n = 2
arr = [1]
print(findMissingElement(n, arr))  # Output: 2
