def reverseWords(s):
    # Split the string into words using '.' as the delimiter
    words = s.split('.')
    
    # Reverse the list of words
    words.reverse()
    
    # Join the reversed list back into a string with '.' as delimiter
    return '.'.join(words)

# Example usage:
str1 = "i.like.this.program.very.much"
print(reverseWords(str1))  # Output: "much.very.program.this.like.i"

str2 = "pqr.mno"
print(reverseWords(str2))  # Output: "mno.pqr"
