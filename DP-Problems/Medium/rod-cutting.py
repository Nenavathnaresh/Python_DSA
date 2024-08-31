def cutRod(price, N):
    # Initialize the dp array with zeros
    dp = [0] * (N + 1)
    
    # Build the dp array from 1 to N
    for i in range(1, N + 1):
        max_val = 0
        for j in range(1, i + 1):
            max_val = max(max_val, price[j - 1] + dp[i - j])
        dp[i] = max_val
    
    return dp[N]

# Example usage:
N1 = 8
price1 = [1, 5, 8, 9, 10, 17, 17, 20]
print(cutRod(price1, N1))  # Output: 22

N2 = 8
price2 = [3, 5, 8, 9, 10, 17, 17, 20]
print(cutRod(price2, N2))  # Output: 24
