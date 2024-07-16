def remainingSubstring(s, ch, count):
    occurrence = 0
    n = len(s)
    
    for i in range(n):
        if s[i] == ch:
            occurrence += 1
            if occurrence == count:
                # Return the substring from the next position to the end
                return s[i + 1:]
    
    # If the character does not occur 'count' times, return an empty string
    return ""

# Example usage:
print(remainingSubstring("Thisisdemostring", 'i', 3))  # Output: "ng"
print(remainingSubstring("Thisisdemostri", 'i', 3))    # Output: ""
print(remainingSubstring("abcd", 'x', 2))              # Output: ""
