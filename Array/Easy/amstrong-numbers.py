def is_armstrong_number(n):
    # Extract digits
    hundreds = n // 100
    tens = (n // 10) % 10
    units = n % 10
    
    # Calculate the sum of the cubes of the digits
    armstrong_sum = hundreds**3 + tens**3 + units**3
    
    # Compare the sum to the original number
    if armstrong_sum == n:
        return "Yes"
    else:
        return "No"
    
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def armstrongNumber (self, n):
        # code here 
        num = n 
        sum = 0
        while n > 0:
            sum += (n % 10) **3 
            n = n // 10 
        if sum == num:    
            return 'Yes'
        else:
            return "No"

# Test the function with example inputs
print(is_armstrong_number(153))  # Output: Yes
print(is_armstrong_number(371))  # Output: Yes
print(is_armstrong_number(372))  # Output: No
print(is_armstrong_number(370))  # Output: Yes
