def countStrings(N):
    MOD = 1000000007
    
    if N == 1:
        return 2
    
    # dp[i][0] -> valid strings of length i ending in 0
    # dp[i][1] -> valid strings of length i ending in 1
    dp0, dp1 = 1, 1  # For N = 1
    
    for i in range(2, N + 1):
        new_dp0 = (dp0 + dp1) % MOD
        new_dp1 = dp0 % MOD
        
        dp0 = new_dp0
        dp1 = new_dp1
    
    return (dp0 + dp1) % MOD

# Example usage:
N = 3
print(countStrings(N))  # Output: 5

######################################################################################  

MOD = 10**9 + 7

def countStrings(N):
    # Base cases
    if N == 1:
        return 2
    if N == 2:
        return 3
    
    # Initialize dp[1] and dp[2]
    prev2 = 2  # dp[1]
    prev1 = 3  # dp[2]
    
    # Fill dp array for all n from 3 to N
    for i in range(3, N + 1):
        curr = (prev1 + prev2) % MOD
        prev2 = prev1
        prev1 = curr
    
    return prev1

# Example Usage
print(countStrings(3))  # Output: 5
print(countStrings(2))  # Output: 3

