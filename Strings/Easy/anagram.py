def isAnagram(s1, s2):
    # If lengths differ, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    # Create a frequency array for 26 lowercase alphabets
    freq = [0] * 26

    # Count characters in s1 and s2
    for i in range(len(s1)):
        freq[ord(s1[i]) - ord('a')] += 1
        freq[ord(s2[i]) - ord('a')] -= 1

    # Check if all frequencies are zero
    for count in freq:
        if count != 0:
            return False

    return True

# Examples
print(isAnagram("geeks", "kseeg"))   # Output: True
print(isAnagram("allergy", "allergic"))  # Output: False
print(isAnagram("g", "g"))           # Output: True

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        freq_a = {} 
        freq_b = {}
        for char in a :
            freq_a[char] = freq_a.get(char, 0) + 1 
        for char in b :
            freq_b[char] = freq_b.get(char, 0) + 1 
        return freq_a == freq_b 
        #code here