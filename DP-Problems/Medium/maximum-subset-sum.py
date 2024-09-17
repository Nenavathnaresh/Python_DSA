from typing import List

class Solution:
    
    # Function to find the maximum subset sum
    def findMaxSubsetSum(self, N: int, A: List[int]) -> int:
        
        # Initializing the dp array with 0
        dp = [[0]*2 for i in range(N+1)]
        dp[0][0], dp[0][1] = 0, 0
        
        # Looping through the elements
        for i in range(1, N+1):
            
            # Calculating the maximum subset sum with and without including the current element
            dp[i][0] = dp[i-1][1]
            dp[i][1] = max(dp[i-1][0]+A[i-1], dp[i-1][1]+A[i-1])
            
        # Returning the maximum subset sum
        return max(dp[N][0], dp[N][1])