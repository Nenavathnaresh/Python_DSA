def maxLength(S):
    n = len(S)
    
    # DP array initialized to 1 for each character
    dp = [1] * n
    
    # Loop to fill the dp array
    for i in range(1, n):
        for j in range(i):
            if S[j] < S[i]:  # Check if the characters form an increasing subsequence
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The result is the maximum value in the dp array
    return max(dp)

# Example usage:
S1 = "abcdapzfqh"
print(maxLength(S1))  # Output: 6

S2 = "hkm"
print(maxLength(S2))  # Output: 3
