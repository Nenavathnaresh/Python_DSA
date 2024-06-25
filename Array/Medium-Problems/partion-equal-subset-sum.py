class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)
        
        # If total_sum is odd, partition is not possible
        if total_sum % 2 != 0:
            return 0
        
        # Target sum is half of the total sum
        target_sum = total_sum // 2
        
        # DP array to keep track of possible sums
        dp = [False] * (target_sum + 1)
        dp[0] = True  # Because we can always have a subset with sum 0
        
        for num in arr:
            # Traverse the dp array from right to left
            for j in range(target_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return 1 if dp[target_sum] else 0

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    N1, arr1 = 4, [1, 5, 11, 5]
    print(solution.equalPartition(N1, arr1))  # Output: 1 (YES)
    
    N2, arr2 = 3, [1, 3, 5]
    print(solution.equalPartition(N2, arr2))  # Output: 0 (NO)
