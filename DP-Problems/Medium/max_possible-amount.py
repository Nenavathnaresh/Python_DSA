def maxAmount(N, arr):
    # Create a dp table where dp[i][j] will store the maximum amount of money
    # Geek can collect from subarray arr[i..j]
    dp = [[0] * N for _ in range(N)]
    
    # Fill the dp table
    for gap in range(N):  # gap is the distance between i and j
        for i in range(N - gap):
            j = i + gap
            if i == j:
                dp[i][j] = arr[i]  # Only one coin left, pick it
            elif j == i + 1:
                dp[i][j] = max(arr[i], arr[j])  # Only two coins, pick the larger one
            else:
                # Calculate the value by picking the first or the last coin
                dp[i][j] = max(
                    arr[i] + min(dp[i+2][j] if i+2 <= j else 0, dp[i+1][j-1] if i+1 <= j-1 else 0),
                    arr[j] + min(dp[i+1][j-1] if i+1 <= j-1 else 0, dp[i][j-2] if i <= j-2 else 0)
                )
    
    # The answer for the full array will be stored in dp[0][N-1]
    return dp[0][N-1]

# Example usage:
N1 = 4
arr1 = [5, 3, 7, 10]
print(maxAmount(N1, arr1))  # Output: 15

N2 = 4
arr2 = [8, 15, 3, 7]
print(maxAmount(N2, arr2))  # Output: 22
