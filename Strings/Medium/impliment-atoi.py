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



########################################################


def atoi(s):
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648

    # Step 1: Remove leading whitespaces
    s = s.strip()
    
    # Step 2: Handle empty string
    if not s:
        return 0
    
    # Step 3: Handle optional sign
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1

    # Step 4: Read digits and ignore leading zeros
    result = 0
    while i < len(s) and '0' <= s[i] <= '9':
        digit = ord(s[i]) - ord('0')  # Convert character to digit
        result = result * 10 + digit

        # Step 5: Check for overflow
        if sign == 1 and result > INT_MAX:
            return INT_MAX
        if sign == -1 and -result < INT_MIN:
            return INT_MIN
        
        i += 1

    # Step 6: Apply the sign and return the result
    return sign * result

# Examples:
print(atoi("-123"))             # Output: -123
print(atoi("  -"))              # Output: 0
print(atoi(" 1231231231311133")) # Output: 2147483647
print(atoi("-999999999999"))     # Output: -2147483648
print(atoi("  -0012gfg4"))       # Output: -12

