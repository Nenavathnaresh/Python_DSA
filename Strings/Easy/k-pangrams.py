class Solution:

    def kPangram(self, string, k):
        noOfAlpha = len(string) - string.count(' ')

        # If the number of alphabets in the string is less than 26, it can't be a pangram.
        if noOfAlpha < 26:
            return False

        # If k is greater than 25, it means any k distinct alphabets can form a pangram.
        if k > 25:
            return True

        # Creating a map to keep track of alphabets present in the string.
        alphabet_map = [0] * 26

        # Iterating over the string to update the map.
        for char in string:
            if char != ' ':
                alphabet_map[ord(char.lower()) - ord('a')] = 1

        # Counting the number of distinct alphabets present in the string.
        noOfDistAlpha = alphabet_map.count(1)

        # If the number of distinct alphabets plus k is greater than or equal to 26,
        # it means k distinct alphabets can be added to the string to form a pangram.
        if noOfDistAlpha + k >= 26:
            return True
        else:
            return False