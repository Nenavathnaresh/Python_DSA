def allPalindromicPerms(s):
    def isPalindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if isPalindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result

# Example usage
s1 = "geeks"
print(allPalindromicPerms(s1))  # Output: [['g', 'e', 'e', 'k', 's'], ['g', 'ee', 'k', 's']]
s2 = "madam"
print(allPalindromicPerms(s2))  # Output: [['m', 'a', 'd', 'a', 'm'], ['m', 'ada', 'm'], ['madam']]
