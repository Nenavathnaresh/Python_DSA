def graycode(N):
    result = []
    num_patterns = 1 << N  # This is 2^N
    
    for i in range(num_patterns):
        # Generate the i-th Gray code
        gray = i ^ (i >> 1)
        # Format the gray code to a binary string of length N
        gray_str = format(gray, 'b').zfill(N)
        result.append(gray_str)
    
    return result

# Example usage:
N = 2
print(graycode(N))  # Output: ['00', '01', '11', '10']

N = 3
print(graycode(N))  # Output: ['000', '001', '011', '010', '110', '111', '101', '100']
