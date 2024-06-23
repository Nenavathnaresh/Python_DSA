def bracket_numbers(s):
    result = []
    stack = []
    counter = 1

    for char in s:
        if char == '(':
            stack.append(counter)
            result.append(counter)
            counter += 1
        elif char == ')':
            num = stack.pop()
            result.append(num)
    
    return result

# Examples
print(bracket_numbers("(aa(bdc))p(dee)"))  # Expected output: [1, 2, 2, 1, 3, 3]
print(bracket_numbers("(((()("))           # Expected output: [1, 2, 3, 4, 4, 5]

# For better clarity, converting the list to a string with space-separated values for easier comparison to the given examples
def format_output(output):
    return ' '.join(map(str, output))

print(format_output(bracket_numbers("(aa(bdc))p(dee)")))  # Expected output: 1 2 2 1 3 3
print(format_output(bracket_numbers("(((()(")))           # Expected output: 1 2 3 4 4 5
