def isInterleave(A, B, C):
    lenA, lenB, lenC = len(A), len(B), len(C)
    
    # If the lengths don't match, it cannot be an interleaving
    if lenA + lenB != lenC:
        return False
    
    # DP table initialization
    dp = [[False] * (lenB + 1) for _ in range(lenA + 1)]
    dp[0][0] = True
    
    # Fill the table
    for i in range(lenA + 1):
        for j in range(lenB + 1):
            if i > 0 and dp[i-1][j] and A[i-1] == C[i+j-1]:
                dp[i][j] = True
            if j > 0 and dp[i][j-1] and B[j-1] == C[i+j-1]:
                dp[i][j] = True
    
    return dp[lenA][lenB]

# Example usage
A = "YX"
B = "X"
C = "XXY"
print(isInterleave(A, B, C))  # Output: False

A = "XY"
B = "X"
C = "XXY"
print(isInterleave(A, B, C))  # Output: True
