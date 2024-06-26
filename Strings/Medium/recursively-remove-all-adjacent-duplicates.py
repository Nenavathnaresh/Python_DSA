class Solution:

    # Function to recursively remove consecutive duplicate characters from a string
    def rremove(self, S):
        new = []  # Initialize a new empty list to store characters without consecutive duplicates
        i = 0  # Initialize a variable to keep track of the current index
        n = len(S)  # Get the length of the string
        
        # Iterate through the string
        while i < len(S):
            flag = 0  # Initialize a flag variable to check if there are consecutive duplicates
            
            # Find consecutive duplicate characters
            while i < n-1 and S[i] == S[i+1]:
                flag = 1  # Set the flag to indicate that there are consecutive duplicates
                i += 1  # Move to the next index

            # If there are no consecutive duplicates, add the character to the new list
            if flag == 0:
                new.append(S[i])
            
            i += 1  # Move to the next index
            
        # If the length of the new list is less than the length of the original string,
        # recursively remove consecutive duplicates from the new list
        if len(new) < n:
            return self.rremove(new)
            
        # Convert the new list into a string and return it
        return ''.join(new)