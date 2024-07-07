def isAdditiveSequence(n):
    def is_valid_number(s):
        # A valid number should not have leading zeros unless it is "0"
        return not (len(s) > 1 and s[0] == '0')

    length = len(n)
    
    # Iterate through possible splits for the first number
    for i in range(1, length):
        # Iterate through possible splits for the second number
        for j in range(i + 1, length):
            num1, num2 = n[:i], n[i:j]
            # Check if both numbers are valid
            if not is_valid_number(num1) or not is_valid_number(num2):
                continue

            num1, num2 = int(num1), int(num2)
            sequence = [num1, num2]
            k = j  # Start of the next number in the sequence

            # Generate the sequence and check against the input string
            while k < length:
                next_num = sequence[-1] + sequence[-2]  # Next number in sequence
                next_num_str = str(next_num)  # Convert to string
                next_len = len(next_num_str)  # Length of the next number string
                
                # Check if the next part of the input string matches the next number
                if k + next_len <= length and n[k:k+next_len] == next_num_str:
                    sequence.append(next_num)  # Add to the sequence
                    k += next_len  # Move to the next part of the string
                else:
                    break  # Break if it doesn't match

            if k == length:  # If we have consumed the entire input string
                return True

    return False
