def minDifference(arr, n):
    # Calculate the total sum of elements in the array
    sumTotal = sum(arr)
    
    # Initialize dp array where dp[j] means whether a subset sum of j is possible
    dp = [False] * (sumTotal + 1)
    dp[0] = True  # A subset with sum 0 is always possible (the empty subset)
    
    # Fill the dp array
    for i in range(n):
        for j in range(sumTotal, arr[i] - 1, -1):
            dp[j] = dp[j] or dp[j - arr[i]]
    
    # Find the minimum difference by checking the closest subset sum to sumTotal // 2
    minDiff = float('inf')
    for j in range(sumTotal // 2 + 1):
        if dp[j]:
            minDiff = min(minDiff, sumTotal - 2 * j)
    
    return minDiff

# Example usage:
arr1 = [1, 6, 11, 5]
n1 = len(arr1)
print(minDifference(arr1, n1))  # Output: 1

arr2 = [1, 4]
n2 = len(arr2)
print(minDifference(arr2, n2))  # Output: 3
