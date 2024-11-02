def multiplyStrings(s1, s2):
    # Step 1: Determine the sign of the result
    negative = (s1[0] == '-') ^ (s2[0] == '-')  # XOR to check if signs are opposite
    if s1[0] in '+-': s1 = s1[1:]  # Remove sign if present
    if s2[0] in '+-': s2 = s2[1:]
    
    # Step 2: Remove leading zeros
    s1 = s1.lstrip('0')
    s2 = s2.lstrip('0')
    
    # If either string is empty after stripping zeros, the result is "0"
    if not s1 or not s2:
        return "0"
    
    n1, n2 = len(s1), len(s2)
    result = [0] * (n1 + n2)  # Result array to store multiplication results
    
    # Step 3: Perform multiplication
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            # Multiply digits
            mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
            # Position in the result array
            pos1, pos2 = i + j, i + j + 1
            # Add to current position
            total = mul + result[pos2]
            
            result[pos2] = total % 10   # Place the unit digit at pos2
            result[pos1] += total // 10  # Carry goes to the next left position
            
    # Step 4: Convert result array to string
    result_str = ''.join(map(str, result)).lstrip('0')  # Remove leading zeros
    
    # If result_str is empty, that means the result is zero
    if not result_str:
        return "0"
    
    # Step 5: Add sign if necessary
    if negative:
        result_str = '-' + result_str
    
    return result_str
