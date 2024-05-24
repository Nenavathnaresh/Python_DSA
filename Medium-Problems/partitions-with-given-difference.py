
def countPartitions(n, d, arr):
    MOD = 10**9 + 7
    
    total_sum = sum(arr)
    
    # Check if (total_sum + d) is even, otherwise return 0
    if (total_sum + d) % 2 != 0:
        return 0
    
    target = (total_sum + d) // 2
    
    # Initialize the DP array
    dp = [0] * (target + 1)
    dp[0] = 1
    
    # Fill the DP array
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = (dp[j] + dp[j - num]) % MOD
    
    return dp[target]

# Example usage:
n1 = 4
d1 = 3
arr1 = [5, 2, 6, 4]
print(countPartitions(n1, d1, arr1))  # Output: 1

n2 = 4
d2 = 0
arr2 = [1, 1, 1, 1]
print(countPartitions(n2, d2, arr2))  # Output: 6
