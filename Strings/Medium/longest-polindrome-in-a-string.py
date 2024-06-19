def longestPalin(S):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    n = len(S)
    if n == 0:
        return ""
    
    longest = ""
    
    for i in range(n):
        # Check for odd-length palindromes
        odd_palindrome = expand_around_center(S, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Check for even-length palindromes
        if i + 1 < n:
            even_palindrome = expand_around_center(S, i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
    
    return longest

# Test cases
print(longestPalin("aaaabbaa"))  # Output: aabbaa
print(longestPalin("abc"))       # Output: a
