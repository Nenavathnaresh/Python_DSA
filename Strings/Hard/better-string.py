def distinctSubsequences(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # base case: empty string has one subsequence (the empty one)

    last_occurrence = {}

    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]  # double the number of subsequences from previous length
        if s[i - 1] in last_occurrence:
            dp[i] -= dp[last_occurrence[s[i - 1]] - 1]  # subtract the duplicate subsequences
        last_occurrence[s[i - 1]] = i  # update last occurrence of the character

    return dp[n] - 1  # exclude the empty subsequence

def betterString(str1, str2):
    if distinctSubsequences(str1) >= distinctSubsequences(str2):
        return str1
    else:
        return str2

# Test cases
print(betterString("gfg", "ggg"))  # Output: "gfg"
print(betterString("a", "b"))      # Output: "a"
