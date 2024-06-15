def count_sequences(n):
    if n == 1:
        return 10

    # Moves dictionary: current digit -> possible next digits
    moves = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [0, 5, 7, 8, 9],
        9: [6, 8, 9]
    }

    # Initialize DP table with dimensions (n+1) x 10
    dp = [[0] * 10 for _ in range(n+1)]

    # Base case: Length 1 sequences
    for j in range(10):
        dp[1][j] = 1

    # Fill the DP table
    for length in range(2, n+1):
        for digit in range(10):
            dp[length][digit] = sum(dp[length-1][prev] for prev in moves[digit])

    # The result is the sum of all sequences of length n
    return sum(dp[n][digit] for digit in range(10))

# Example usage
print(count_sequences(1))  # Output: 10
print(count_sequences(2))  # Output: 36
print(count_sequences(3))  # Output: 138
