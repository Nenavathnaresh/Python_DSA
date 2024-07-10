def permutation(s):
    def backtrack(index, path):
        if index == len(s):
            result.append("".join(path))
            return
        # Include the current character without a preceding space
        backtrack(index + 1, path + [s[index]])
        # Include the current character with a preceding space if not the first character
        if index > 0:
            backtrack(index + 1, path + [' ', s[index]])
    
    result = []
    # Start the backtracking from the first character
    backtrack(1, [s[0]])
    result.sort()  # Sort the result lexicographically
    return result

# Example usage:
s1 = "ABC"
print(permutation(s1))  # Output: ['A B C', 'A BC', 'AB C', 'ABC']

s2 = "BBR"
print(permutation(s2))  # Output: ['B B R', 'B BR', 'BB R', 'BBR']
