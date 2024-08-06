class Solution:
    def isValid(self, s):
        # Split the address into parts by dots
        parts = s.split('.')
        
        # Check if there are exactly 4 parts
        if len(parts) != 4:
            return 0
        
        for part in parts:
            # Check if the part is a digit
            if not part.isdigit():
                return 0
            
            # Convert the part to an integer
            num = int(part)
            
            # Check if the integer is in the range [0, 255]
            if num < 0 or num > 255:
                return 0
            
            # Check for leading zeros
            if part != str(num):
                return 0
        
        return 1

# Example usage:
solution = Solution()
print(solution.isValid("222.111.111.111"))  # Output: 1
print(solution.isValid("5555..555"))        # Output: 0

##############################################################################################

class Solution:
    def isValid(self, str):
        #code here
        split_str = str.split(".")
        
        if len(split_str) != 4 :
            return False
        for num in split_str:
            if int(num) > 255:
                return False
        return True

