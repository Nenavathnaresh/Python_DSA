def is_sum_string(S):
    def is_valid_sum_string(S, start, len1, len2):
        num1 = S[start:start+len1]
        num2 = S[start+len1:start+len1+len2]
        sum_len = max(len(num1), len(num2))
        sum_val = str(int(num1) + int(num2))
        
        if start + len1 + len2 + len(sum_val) > len(S):
            return False
        
        num3 = S[start + len1 + len2: start + len1 + len2 + len(sum_val)]
        
        if sum_val != num3:
            return False
        
        if start + len1 + len2 + len(sum_val) == len(S):
            return True
        
        return is_valid_sum_string(S, start + len1, len2, len(sum_val))
    
    n = len(S)
    
    for len1 in range(1, n):
        for len2 in range(1, n - len1):
            if is_valid_sum_string(S, 0, len1, len2):
                return 1
    
    return 0

# Example usage
print(is_sum_string("12243660"))  # Output: 1
print(is_sum_string("1111112223"))  # Output: 1
print(is_sum_string("123456"))     # Output: 0
