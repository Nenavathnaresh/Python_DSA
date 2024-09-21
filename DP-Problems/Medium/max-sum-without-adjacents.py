def findMaxSum(arr, n):
    # Base case when there are no elements
    if n == 0:
        return 0
    
    # Initialize two variables
    incl = arr[0]  # Sum including the first element
    excl = 0       # Sum excluding the first element
    
    # Traverse the array starting from the second element
    for i in range(1, n):
        # Current maximum excluding the current element
        new_excl = max(incl, excl)
        
        # Current maximum including the current element
        incl = excl + arr[i]
        
        # Update excl to new_excl for the next iteration
        excl = new_excl
    
    # The answer is the maximum of incl and excl
    return max(incl, excl)

# Example usage:
arr1 = [5, 5, 10, 100, 10, 5]
n1 = len(arr1)
print(findMaxSum(arr1, n1))  # Output: 110

arr2 = [3, 2, 7, 10]
n2 = len(arr2)
print(findMaxSum(arr2, n2))  # Output: 13
