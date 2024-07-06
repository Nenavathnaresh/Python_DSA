def decodedString(s):
    stack = []  # Stack to keep track of strings and repeat counts
    current_num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            # Build the number
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push the current number and string to the stack
            stack.append((current_str, current_num))
            # Reset the current string and number
            current_str = ""
            current_num = 0
        elif char == ']':
            # Pop from the stack and repeat the current string
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            # Build the current string
            current_str += char
    
    return current_str

# Example usage:
s = "3[b2[ca]]"
print(decodedString(s))  # Output: "bcacabcacabcaca"

s = "1[b]"
print(decodedString(s))  # Output: "b"
