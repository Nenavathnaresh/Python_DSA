def longestSubstring(S):
    n = len(S)
    max_len = 0
    
    # Hashmap to store the first occurrence of each bitmask
    dp = {0: -1}
    
    # This bitmask will track the parity (odd/even) of frequencies
    bitmask = 0
    
    for i in range(n):
        # Update the bitmask for the current character
        char_index = ord(S[i]) - ord('a')
        bitmask ^= (1 << char_index)
        
        # If this bitmask has been seen before, calculate the length of the substring
        if bitmask in dp:
            max_len = max(max_len, i - dp[bitmask])
        else:
            dp[bitmask] = i
        
        # Check for substrings where only one character has an odd count
        for j in range(26):
            modified_bitmask = bitmask ^ (1 << j)
            if modified_bitmask in dp:
                max_len = max(max_len, i - dp[modified_bitmask])
    
    return max_len

# Example usage:
S = "rwkrnw"
print(longestSubstring(S))  # Output: 1
