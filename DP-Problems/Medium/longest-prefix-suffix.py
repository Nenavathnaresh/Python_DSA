def longestPrefixSuffix(s):
    n = len(s)
    
    # Create the LPS (Longest Prefix Suffix) array
    lps = [0] * n  # lps[i] stores the length of the longest prefix-suffix for s[0..i]
    
    length = 0  # length of the previous longest prefix-suffix
    i = 1
    
    # The LPS array building process
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # This is tricky. Consider the example "AAACAAAA" and i = 7.
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    # lps[n-1] will contain the length of the longest proper prefix
    # which is also a suffix for the entire string
    return lps[n - 1]

# Example usage:
s1 = "abab"
print(longestPrefixSuffix(s1))  # Output: 2

s2 = "aaaa"
print(longestPrefixSuffix(s2))  # Output: 3
