def FindMaxSum(arr, n):
    # Base cases
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    
    # Create a dp array of size n
    dp = [0] * n
    
    # Initialize the first two elements
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    
    # Fill the dp array using the recurrence relation
    for i in range(2, n):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    
    # The last element of dp array is the answer
    return dp[-1]
# Example usage:
arr = [6, 5, 5, 7, 4]
n = len(arr)
print(FindMaxSum(arr, n))  # Output: 15

arr = [1, 5, 3]
n = len(arr)
print(FindMaxSum(arr, n))  # Output: 5

#######################################################################################

def FindMaxSum(arr, n):
    # Base cases
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    
    # Initialize the two variables for the two previous values
    prev2 = arr[0]
    prev1 = max(arr[0], arr[1])
    
    # Compute the maximum sum using the recurrence relation
    for i in range(2, n):
        current = max(prev1, arr[i] + prev2)
        prev2 = prev1
        prev1 = current
    
    # The last computed value is the answer
    return prev1

# Example usage:
arr = [6, 5, 5, 7, 4]
n = len(arr)
print(FindMaxSum(arr, n))  # Output: 15

arr = [1, 5, 3]
n = len(arr)
print(FindMaxSum(arr, n))  # Output: 5


