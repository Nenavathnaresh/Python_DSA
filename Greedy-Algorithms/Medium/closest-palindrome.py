def closestPalindrome(num):
    def is_palindrome(x):
        return str(x) == str(x)[::-1]
    
    def generate_palindromes(n):
        s = str(n)
        length = len(s)
        half = (length + 1) // 2
        prefix = int(s[:half])
        
        # Generate direct mirrored palindrome
        palindromes = [
            int(str(prefix) + str(prefix)[:length//2][::-1]),
            int(str(prefix-1) + str(prefix-1)[:length//2][::-1]),
            int(str(prefix+1) + str(prefix+1)[:length//2][::-1])
        ]
        
        # Handle edge cases for very small or very large numbers
        lower_power = 10**(length-1) - 1  # e.g., 999 for 1000
        higher_power = 10**length + 1     # e.g., 10001 for 10000
        palindromes.extend([lower_power, higher_power])
        
        return palindromes
    
    if is_palindrome(num):
        return num
    
    candidates = generate_palindromes(num)
    closest = None
    min_diff = float('inf')
    
    for candidate in candidates:
        if candidate != num:
            diff = abs(candidate - num)
            if diff < min_diff or (diff == min_diff and candidate < closest):
                min_diff = diff
                closest = candidate
    
    return closest

# Example usage:
print(closestPalindrome(9))   # Output: 9
print(closestPalindrome(489)) # Output: 484
