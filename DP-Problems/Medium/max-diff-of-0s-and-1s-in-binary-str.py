def maxSubstring(S):
    # Edge case: If the string contains only 1s, return -1
    if '0' not in S:
        return -1
    
    # Initialize variables for Kadane's algorithm
    max_so_far = float('-inf')
    max_ending_here = 0
    
    # Iterate over the binary string
    for char in S:
        # Treat '0' as +1 and '1' as -1
        value = 1 if char == '0' else -1
        max_ending_here += value
        
        # If the sum is greater than the max so far, update max_so_far
        max_so_far = max(max_so_far, max_ending_here)
        
        # If the current sum becomes negative, reset it to 0
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far

# Example usage:
S1 = "11000010001"
print(maxSubstring(S1))  # Output: 6

S2 = "111111"
print(maxSubstring(S2))  # Output: -1
    