def isBalanced(expression: str) -> bool:
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    # Traverse through the expression
    for char in expression:
        if char in '({[':  # If it's an opening bracket, push to stack
            stack.append(char)
        elif char in ')}]':  # If it's a closing bracket
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # Pop the matching opening bracket
            else:
                return False  # Unbalanced if no matching opening bracket
    
    # If stack is empty, it's balanced
    return len(stack) == 0

# Driver code for testing
expression1 = "{([])}"
expression2 = "[(])"
expression3 = "()"
expression4 = "([]"

print("balanced" if isBalanced(expression1) else "not balanced")  # Output: balanced
print("balanced" if isBalanced(expression2) else "not balanced")  # Output: not balanced
print("balanced" if isBalanced(expression3) else "not balanced")  # Output: balanced
print("balanced" if isBalanced(expression4) else "not balanced")  # Output: not balanced
