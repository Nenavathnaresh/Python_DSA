def maxSumIS(arr, n):
    # Initialize the dp array with the values of the array
    dp = [arr[i] for i in range(n)]
    
    # Fill the dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]
    
    # The answer will be the maximum value in dp array
    return max(dp)

# Example usage:
arr = [1, 101, 2, 3, 100]
n = len(arr)
print(maxSumIS(arr, n))  # Output: 106

arr = [4, 1, 2, 3]
n = len(arr)
print(maxSumIS(arr, n))  # Output: 6
