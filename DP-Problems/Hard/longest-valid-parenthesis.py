def longestValidParentheses(s: str) -> int:
    stack = [-1]  # Initialize with -1 to handle base case
    max_length = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)  # Push index of '('
        else:
            stack.pop()  # Pop the top index
            if len(stack) == 0:
                stack.append(i)  # If stack is empty, push the current index
            else:
                max_length = max(max_length, i - stack[-1])  # Calculate valid length
    
    return max_length


####################################################################################################

def longestValidParentheses(s: str) -> int:
    n = len(s)
    dp = [0] * n
    max_length = 0
    
    for i in range(1, n):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2 if i >= 2 else 2
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2 if i - dp[i - 1] - 2 >= 0 else dp[i - 1] + 2
            
            max_length = max(max_length, dp[i])
    
    return max_length
