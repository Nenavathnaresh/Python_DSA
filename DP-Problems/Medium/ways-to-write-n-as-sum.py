MOD = 10**9 + 7

def countPartitions(n):
    # Initialize a 1D DP array of size (n+1)
    dp = [0] * (n + 1)
    
    # Base case: 1 way to partition 0 (the empty partition)
    dp[0] = 1

    # Fill the dp array using the optimized space method
    for j in range(1, n):  # Loop over possible parts (up to n-1)
        for i in range(j, n + 1):  # Loop over total sum (1 to n)
            dp[i] = (dp[i] + dp[i - j]) % MOD

    # The answer is dp[n], which stores the number of partitions of n using numbers up to n-1
    return dp[n]

# Example usage:
n1 = 5
print(countPartitions(n1))  # Output: 6

n2 = 3
print(countPartitions(n2))  # Output: 2
