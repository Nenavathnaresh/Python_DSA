def arrangeTiles(N):
    # Base case for grids smaller than 4
    if N == 0:
        return 1
    if N == 1 or N == 2 or N == 3:
        return 1
    if N == 4:
        return 2
    
    # Initialize dp array for storing results up to N
    dp = [0] * (N + 1)
    
    # Base cases
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    
    # Fill dp array for each grid size from 5 to N
    for i in range(5, N + 1):
        dp[i] = dp[i - 1] + dp[i - 4]
    
    return dp[N]

# Example usage:
print(arrangeTiles(1))  # Output: 1
print(arrangeTiles(4))  # Output: 2
print(arrangeTiles(5))  # Output: 3
print(arrangeTiles(8))  # Output: 5
