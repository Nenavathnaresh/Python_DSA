def countFriendsPairings(N):
    MOD = 10**9 + 7

    if N <= 2:
        return N

    # Initialize the first two values
    a, b = 1, 2

    # Fill the DP array iteratively
    for i in range(3, N + 1):
        c = (b + (i - 1) * a) % MOD
        a, b = b, c

    return b

# Example usage:
N = 3
print(countFriendsPairings(N))  # Output: 4

N = 2
print(countFriendsPairings(N))  # Output: 2
