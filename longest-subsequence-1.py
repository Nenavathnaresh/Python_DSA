def longestSubseq(n, a):
    # Initialize dp array where each element is at least 1
    dp = [1] * n
    
    # Fill dp array using dynamic programming
    for i in range(1, n):
        for j in range(i):
            if abs(a[i] - a[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The answer is the maximum value in the dp array
    return max(dp)

# Example usage:
n1 = 7
a1 = [10, 9, 4, 5, 4, 8, 6]
print(longestSubseq(n1, a1))  # Output: 3

n2 = 5
a2 = [1, 2, 3, 4, 5]
print(longestSubseq(n2, a2))  # Output: 5
