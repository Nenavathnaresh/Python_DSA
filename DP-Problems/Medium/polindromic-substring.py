def longestPalindrome(S):
    def expandAroundCenter(s, left, right):
        # Expand around the center and check for palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring
        return s[left + 1:right]

    n = len(S)
    if n == 0:
        return ""
    
    longest_palindrome = ""
    
    for i in range(n):
        # Check for odd-length palindrome (centered at i)
        palindrome_odd = expandAroundCenter(S, i, i)
        # Check for even-length palindrome (centered between i and i+1)
        palindrome_even = expandAroundCenter(S, i, i + 1)
        
        # Update longest palindrome if needed
        if len(palindrome_odd) > len(longest_palindrome):
            longest_palindrome = palindrome_odd
        if len(palindrome_even) > len(longest_palindrome):
            longest_palindrome = palindrome_even
    
    return longest_palindrome
