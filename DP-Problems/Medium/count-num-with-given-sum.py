class Solution:
    # Function to count the number of ways to reach the given score in a game.
    def countWays(self, n, Sum):
        MOD = 1000000007
        dp = [[0] * (Sum + 1) for _ in range(n)]
        
        # Initialize for the first row
        for s in range(1, min(Sum + 1, 10)):
            dp[0][s] = 1
        
        # Fill the dp table
        for i in range(1, n):
            for s in range(1, Sum + 1):
                for digit in range(min(s, 10)):
                    if s > digit:
                        dp[i][s] = (dp[i][s] + dp[i - 1][s - digit]) % MOD
        
        return -1 if dp[n - 1][Sum] == 0 else dp[n - 1][Sum]

# Example usage:
sol = Solution()
print(sol.countWays(2, 10))  # Replace with the actual n and Sum
