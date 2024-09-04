def countWays(n):
    # Initialize dp array
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # 1 way to stay at the bottom (do nothing)
    dp[1] = 1  # 1 way to reach the first stair (single step)
    
    # Fill the dp array
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # The problem boils down to distinct number of combinations
    # which is simply n//2 + 1
    return n // 2 + 1

# Example usage:
print(countWays(4))  # Output: 3
print(countWays(5))  # Output: 3


###################################################################################


def countWays(n):
    return n // 2 + 1

# Example usage:
print(countWays(4))  # Output: 3
print(countWays(5))  # Output: 3
