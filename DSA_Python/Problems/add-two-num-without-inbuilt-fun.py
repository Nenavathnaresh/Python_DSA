def add(a, b):
    # Initialize the result and carry
    result = 0
    carry = 0
    place = 1  # This will track the place (1's, 10's, 100's, etc.)

    # Loop until both numbers and carry are zero
    while a != 0 or b != 0 or carry != 0:
        # Get the last digit of a and b
        digit_a = a % 10
        digit_b = b % 10
        
        # Add the digits and the carry
        sum_digits = digit_a + digit_b + carry
        
        # If the sum is 10 or greater, we have a carry for the next digit
        if sum_digits >= 10:
            carry = 1
            sum_digits -= 10
        else:
            carry = 0
        
        # Add the current sum to the result (considering the place)
        result += sum_digits * place
        
        # Move to the next digit (shift numbers to the right)
        a //= 10
        b //= 10
        place *= 10  # Move the place value to the next (1's, 10's, 100's, etc.)

    return result

# Test the function with the given numbers
a = 984
b = 798
result = add(a, b)
print(f"The sum of {a} and {b} is: {result}")
