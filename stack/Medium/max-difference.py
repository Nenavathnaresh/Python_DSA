def maxAbsDiff(arr):
    n = len(arr)
    
    # Arrays to store left and right smaller elements
    ls = [0] * n
    rs = [0] * n
    
    # Stack to keep track of the nearest smaller elements
    stack = []
    
    # Calculate left smaller elements
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            ls[i] = arr[stack[-1]]
        else:
            ls[i] = 0
        stack.append(i)
    
    # Clear the stack for right smaller elements calculation
    stack.clear()
    
    # Calculate right smaller elements
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            rs[i] = arr[stack[-1]]
        else:
            rs[i] = 0
        stack.append(i)
    
    # Find the maximum absolute difference
    max_diff = 0
    for i in range(n):
        max_diff = max(max_diff, abs(ls[i] - rs[i]))
    
    return max_diff

# Example usage:
arr1 = [2, 1, 8]
arr2 = [2, 4, 8, 7, 7, 9, 3]
print(maxAbsDiff(arr1))  # Output: 1
print(maxAbsDiff(arr2))  # Output: 4
