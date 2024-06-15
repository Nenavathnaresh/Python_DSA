def possibleWords(a, N):
    # Mapping of digits to corresponding letters on the keypad
    keypad = {
        2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
        7: "pqrs", 8: "tuv", 9: "wxyz"
    }
    
    # Result list to store all possible words
    result = []
    
    # Helper function to perform the recursion
    def backtrack(index, current_combination):
        # If the current combination has reached the length of the input array
        if index == N:
            result.append(current_combination)
            return
        
        # Get the current digit from the input array
        current_digit = a[index]
        
        # Iterate through each character corresponding to the current digit
        for char in keypad[current_digit]:
            # Append the character to the current combination and recurse for the next digit
            backtrack(index + 1, current_combination + char)
    
    # Initialize the recursion with the first digit (index 0) and an empty combination
    backtrack(0, "")
    
    # Return the list of possible words
    return result

# Example usage
N1 = 3
a1 = [2, 3, 4]
print(possibleWords(a1, N1))

N2 = 3
a2 = [3, 4, 5]
print(possibleWords(a2, N2))
