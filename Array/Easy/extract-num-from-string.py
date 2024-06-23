def largest_number_without_nine(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Extract numbers and filter out those containing '9'
    valid_numbers = []
    for word in words:
        if word.isdigit() and '9' not in word:
            valid_numbers.append(int(word))
    
    # Return the maximum number or -1 if no valid number exists
    if valid_numbers:
        return max(valid_numbers)
    else:
        return -1

# Examples
print(largest_number_without_nine("This is alpha 5057 and 97"))  # Expected output: 5057
print(largest_number_without_nine("Another input 9007"))        # Expected output: -1
print(largest_number_without_nine("Here is a test 123 456 7890")) # Expected output: 456
print(largest_number_without_nine("All numbers 99 999 9999"))    # Expected output: -1
