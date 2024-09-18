def CountPS(s, n):
    # Initialize a table to store whether substrings are palindromes
    dp = [[False] * n for _ in range(n)]
    
    count = 0
    
    # Check for palindromes of length 1 (they don't count towards our result)
    # and length 2
    for i in range(n):
        dp[i][i] = True  # Every single character is a palindrome
        
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1  # Since the length is 2, it's a valid palindrome
    
    # Check for palindromes of length greater than 2
    for length in range(3, n + 1):  # Substring lengths from 3 to n
        for i in range(n - length + 1):  # Starting index of the substring
            j = i + length - 1  # Ending index of the substring
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1
    
    return count

# Example usage:
n = 5
s = "abaab"
print(CountPS(s, n))  # Output: 3

n = 7
s = "abbaeae"
print(CountPS(s, n))  # Output: 4
