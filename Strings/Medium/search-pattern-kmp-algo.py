def findPatternIndices(txt, pat):
    n = len(txt)
    m = len(pat)
    result = []

    # Iterate through the text and compare substrings with the pattern
    for i in range(n - m + 1):
        if txt[i:i + m] == pat:
            result.append(i)

    return result

# Test cases
print(findPatternIndices("abcab", "ab"))  # Output: [0, 3]
print(findPatternIndices("abesdu", "edu"))  # Output: []
print(findPatternIndices("aabaacaadaabaaba", "aaba"))  # Output: [0, 9, 12]
