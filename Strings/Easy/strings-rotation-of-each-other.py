def isRotated(s1, s2):
    # Check if lengths are equal
    if len(s1) != len(s2):
        return False

    # Concatenate s1 with itself
    concatenated = s1 + s1

    # Check if s2 is a substring of concatenated
    return s2 in concatenated

# Example Test Cases
print(isRotated("mightandmagic", "andmagicmigth"))  # Output: False
print(isRotated("abcd", "cdab"))                   # Output: True
print(isRotated("aab", "aba"))                     # Output: True
print(isRotated("abcd", "acbd"))                   # Output: False
