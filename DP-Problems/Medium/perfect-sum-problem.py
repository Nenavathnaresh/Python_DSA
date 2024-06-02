MOD = 10**9 + 7

def perfectSum(N, arr, sum):
    # Create a 2D dp array with (N+1) rows and (sum+1) columns
    dp = [[0] * (sum + 1) for _ in range(N + 1)]
    
    # Initialize dp[0][0] to 1 (one way to get a sum of 0 - the empty subset)
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(1, N + 1):
        for j in range(sum + 1):
            # Exclude the current element
            dp[i][j] = dp[i-1][j]
            
            # Include the current element (if it does not exceed the current sum j)
            if j >= arr[i-1]:
                dp[i][j] = (dp[i][j] + dp[i-1][j - arr[i-1]]) % MOD
    
    # The answer is the number of ways to get the sum using all elements
    return dp[N][sum]

# Example usage:
N1, arr1, sum1 = 6, [5, 2, 3, 10, 6, 8], 10
print(perfectSum(N1, arr1, sum1))  # Output: 3

N2, arr2, sum2 = 5, [2, 5, 1, 4, 3], 10
print(perfectSum(N2, arr2, sum2))  # Output: 3
