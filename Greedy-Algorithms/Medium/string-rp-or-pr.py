def solve(X, Y, S):
    def remove_and_score(s, sub, score):
        stack = []
        total_score = 0
        for char in s:
            if stack and stack[-1] + char == sub:
                stack.pop()
                total_score += score
            else:
                stack.append(char)
        return ''.join(stack), total_score

    if X >= Y:
        # Remove "pr" first
        remaining_string, score1 = remove_and_score(S, "pr", X)
        _, score2 = remove_and_score(remaining_string, "rp", Y)
    else:
        # Remove "rp" first
        remaining_string, score1 = remove_and_score(S, "rp", Y)
        _, score2 = remove_and_score(remaining_string, "pr", X)
    
    return score1 + score2

# Example usage:
print(solve(5, 4, "abppprrr"))  # Output: 15
print(solve(7, 7, "prpptppr"))  # Output: 14
