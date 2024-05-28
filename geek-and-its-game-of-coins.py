def findWinner(n, x, y):
    # Create a dp array to store the winning state
    dp = [0] * (n + 1)
    
    # Base case: dp[0] is 0 since no coins left means the player loses
    dp[0] = 0
    
    # Fill dp array
    for i in range(1, n + 1):
        if i >= 1 and dp[i - 1] == 0:
            dp[i] = 1
        elif i >= x and dp[i - x] == 0:
            dp[i] = 1
        elif i >= y and dp[i - y] == 0:
            dp[i] = 1
        else:
            dp[i] = 0
    
    return dp[n]

# Example usage:
n = 5
x = 3
y = 4
print(findWinner(n, x, y))  # Output: 1 (Geek can win)

n = 2
x = 3
y = 4
print(findWinner(n, x, y))  # Output: 0 (Geek cannot win)
