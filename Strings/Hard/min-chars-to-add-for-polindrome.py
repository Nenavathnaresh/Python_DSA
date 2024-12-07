def minCharsToMakePalindrome(s):
    # Reverse the string
    reversed_s = s[::-1]

    # Combine original and reversed string with a separator
    combined = s + "#" + reversed_s

    # Compute LPS array
    n = len(combined)
    lps = [0] * n

    j = 0  # Length of the previous longest prefix suffix
    for i in range(1, n):
        while j > 0 and combined[i] != combined[j]:
            j = lps[j - 1]
        if combined[i] == combined[j]:
            j += 1
        lps[i] = j

    # Minimum characters to add
    return len(s) - lps[-1]

# Example Test Cases
print(minCharsToMakePalindrome("abc"))  # Output: 2
print(minCharsToMakePalindrome("aacecaaaa"))  # Output: 2
