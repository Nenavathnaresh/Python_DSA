class Solution:

    def roundToNearest(self, num_str: str) -> str:
        n = len(num_str)

        # If the last digit is less than or equal to 5
        # then it can be rounded to the nearest (previous) multiple of 10
        # by just replacing the last digit with 0
        if int(num_str[-1]) <= 5:
            # Set the last digit to 0
            num_str = num_str[:-1] + '0'
            return num_str

        # The number has to be rounded to the next multiple of 10
        else:
            # Replace the last digit with 0
            num_str = num_str[:-1] + '0'
            carry = 1

            # Starting from the second last digit, add 1 to digits while there is carry
            num_str_list = list(num_str)
            i = n - 2
            while i >= 0 and carry == 1:
                current_digit = int(num_str_list[i]) + carry

                # If the digit exceeds 9 then the carry will be generated
                if current_digit > 9:
                    carry = 1
                    current_digit = 0
                else:
                    carry = 0

                # Update the current digit
                num_str_list[i] = str(current_digit)
                i -= 1

            # If the carry is still 1 then it must be inserted at the beginning of the string
            if carry == 1:
                num_str_list.insert(0, '1')

            return ''.join(num_str_list)