def minSteps(s: str) -> int:
    n = len(s)
    
    # dp[i] will store the minimum steps required to form s[0:i+1]
    dp = [float('inf')] * n
    dp[0] = 1  # It takes 1 move to add the first character
    
    for i in range(1, n):
        # Option 1: Add the next character individually
        dp[i] = dp[i - 1] + 1
        
        # Option 2: Check if we can append a prefix to speed up
        # Check if S[0:(i+1)//2] is repeatable to form S[0:i+1]
        for j in range((i + 1) // 2):
            if s[0:j+1] == s[j+1:2*(j+1)]:
                dp[2*(j+1) - 1] = min(dp[2*(j+1) - 1], dp[j] + 1)
    
    return dp[n - 1]
