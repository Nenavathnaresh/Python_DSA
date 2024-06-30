def subsetSums(arr, n):
    def helper(index, current_sum):
        if index == n:
            sums.append(current_sum)
            return
        # Include the current element
        helper(index + 1, current_sum + arr[index])
        # Exclude the current element
        helper(index + 1, current_sum)
    
    sums = []
    helper(0, 0)
    return sums

# Example usage:
arr1 = [2, 3]
n1 = len(arr1)
print(subsetSums(arr1, n1))  # Output: [0, 3, 2, 5]

arr2 = [5, 2, 1]
n2 = len(arr2)
print(subsetSums(arr2, n2))  # Output: [0, 1, 2, 3, 5, 6, 7, 8]
