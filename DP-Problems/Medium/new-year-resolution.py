def isPossible(N, coins):
    MOD = 2024
    # DP array of size MOD + 1 (since sum of coins <= 2024)
    dp = [False] * (MOD + 1)
    dp[0] = True  # We can always make a sum of 0 by taking no coins

    for coin in coins:
        # Traverse backwards to avoid using the same coin multiple times
        for sum_so_far in range(MOD, coin - 1, -1):
            if dp[sum_so_far - coin]:
                dp[sum_so_far] = True

    # Check if there's any sum divisible by 20, 24, or exactly 2024
    for sum_so_far in range(MOD + 1):
        if dp[sum_so_far] and (sum_so_far % 20 == 0 or sum_so_far % 24 == 0 or sum_so_far == MOD):
            return 1  # True, eligible for merchandise

    return 0  # False, not eligible
