def waterOverflow(K, R, C):
    # Initialize a 2D DP array with zeroes, large enough to hold K rows
    dp = [[0] * (r + 1) for r in range(K)]
    
    # Pour K units of water into the top glass
    dp[0][0] = K
    
    # Simulate the water overflow from the top to the bottom
    for r in range(K - 1):
        for c in range(r + 1):
            # If the current glass has more than 1 unit of water, it overflows
            if dp[r][c] > 1:
                excess = dp[r][c] - 1
                dp[r][c] = 1  # Retain only 1 unit of water in the current glass
                
                # Spread the excess water to the next row, to the left and right glasses
                dp[r + 1][c] += excess / 2
                dp[r + 1][c + 1] += excess / 2

    # Return the amount of water in the Rth row and Cth glass, with precision up to 6 decimal places
    return min(1, dp[R - 1][C - 1])

# Example usage:
K1, R1, C1 = 3, 2, 1
print("{:.6f}".format(waterOverflow(K1, R1, C1)))  # Output: 1.000000

K2, R2, C2 = 3, 2, 2
print("{:.6f}".format(waterOverflow(K2, R2, C2)))  # Output: 1.000000
