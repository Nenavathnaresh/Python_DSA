from collections import defaultdict

def smallestWindow(s, p):
    # Edge case: if p is longer than s, it's impossible to have a valid window
    if len(p) > len(s):
        return "-1"
    
    # Step 1: Create a frequency map for p
    p_count = defaultdict(int)
    for char in p:
        p_count[char] += 1

    # Step 2: Initialize the window variables
    window_count = defaultdict(int)
    required = len(p_count)  # number of distinct characters needed
    formed = 0  # number of distinct characters that match their frequency
    
    left, right = 0, 0
    min_length = float('inf')
    min_window = ""
    
    # Step 3: Start sliding the window
    while right < len(s):
        # Add character at right to the window
        char_right = s[right]
        window_count[char_right] += 1
        
        # Check if this character meets the requirement of frequency in p
        if char_right in p_count and window_count[char_right] == p_count[char_right]:
            formed += 1
        
        # Step 4: Try to shrink the window from the left
        while left <= right and formed == required:
            char_left = s[left]
            
            # Check if this is the smallest window so far
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right+1]
            
            # Now shrink the window by removing the left character
            window_count[char_left] -= 1
            if char_left in p_count and window_count[char_left] < p_count[char_left]:
                formed -= 1
            
            left += 1
        
        # Expand the window from the right
        right += 1
    
    # Step 5: Return the result
    return min_window if min_length != float('inf') else "-1"

# Example usage
s = "timetopractice"
p = "toc"
print(smallestWindow(s, p))  # Output: "toprac"

s = "zoomlazapzo"
p = "oza"
print(smallestWindow(s, p))  # Output: "apzo"
    