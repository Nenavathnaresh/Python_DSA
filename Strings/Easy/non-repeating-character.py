class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        freq = {}
        for char in s:
            freq[char] = freq.get(char,0) + 1
            
        for k,v in freq.items():
            if v == 1:
                return k
        return "$"
    

##############################################################

def firstNonRepeatingChar(s):
    # Frequency dictionary to count character occurrences
    freq = {}

    # Count the frequency of each character in the string
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find the first non-repeating character
    for ch in s:
        if freq[ch] == 1:
            return ch

    # If no non-repeating character is found, return '$'
    return '$'

# Test cases
print(firstNonRepeatingChar("geeksforgeeks"))  # Output: f
print(firstNonRepeatingChar("racecar"))        # Output: e
print(firstNonRepeatingChar("aabbccc"))        # Output: $
