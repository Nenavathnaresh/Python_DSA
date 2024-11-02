def my_atoi(s):
    # Define 32-bit integer limits
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    # Step 1: Trim leading whitespaces
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    
    # Step 2: Check if the string is empty after removing whitespaces
    if i == len(s):
        return 0
    
    # Step 3: Handle the sign
    sign = 1
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
    
    # Step 4: Convert digits to an integer
    result = 0
    while i < len(s) and '0' <= s[i] <= '9':
        digit = ord(s[i]) - ord('0')
        
        # Step 5: Handle overflow and underflow
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        i += 1
    
    return sign * result
