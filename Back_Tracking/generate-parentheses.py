def AllParenthesis(N):
    def backtrack(curr, open_count, close_count):
        # Base case: if the current string length is 2 * N, add to the result
        if len(curr) == 2 * N:
            result.append(curr)
            return
        # If we can add an opening parenthesis, do it
        if open_count < N:
            backtrack(curr + '(', open_count + 1, close_count)
        # If we can add a closing parenthesis, do it
        if close_count < open_count:
            backtrack(curr + ')', open_count, close_count + 1)
    
    result = []
    backtrack('', 0, 0)
    return result

# Example usage:
print(AllParenthesis(3))  # Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
print(AllParenthesis(1))  # Output: ['()']
