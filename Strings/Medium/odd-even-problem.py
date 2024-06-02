def evenOdd(s):
    # Create a frequency dictionary manually
    freq = {}
    
    for char in s:
    #     if char in freq:
    #         freq[char] += 1
    #     else:
    #         freq[char] = 1
        freq[char] = freq.get(char,0)+1 

    
    x = 0  # Count for even position characters with even frequency
    y = 0  # Count for odd position characters with odd frequency
    
    # Iterate through each character and its frequency
    for char, count in freq.items():
        # Determine the position of the character in the alphabet
        pos = ord(char) - ord('a') + 1
        
        # Check conditions for x and y
        if pos % 2 == 0 and count % 2 == 0:
            x += 1
        elif pos % 2 == 1 and count % 2 == 1:
            y += 1
    
    # Check if the sum of x and y is even or odd
    if (x + y) % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Example usage
s1 = "abbbcc"
print(evenOdd(s1))  # Output: ODD

s2 = "nobitaa"
print(evenOdd(s2))  # Output: EVEN
