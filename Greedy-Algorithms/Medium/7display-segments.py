class Solution:
    # Function to solve the seven segments problem
    def sevenSegments(self, S: str, N: int) -> str:
        # Dictionary to store the number of segments required for each digit
        f = {
            0: 6,
            1: 2,
            2: 5,
            3: 5,
            4: 4,
            5: 5,
            6: 6,
            7: 3,
            8: 7,
            9: 5
        }
        
        # Variable to store the sum of segments required for all digits
        total_segments = 0
        
        # Calculate the sum of segments required for all digits in S
        for char in S:
            total_segments += f[int(char)]
        
        # String to store the resulting digits
        ans = ""

        # Loop through each digit position
        for i in range(N):
            # Loop through all possible digits
            for j in range(10):
                # Check if it is possible to form the remaining segments
                remaining_segments = total_segments - f[j]
                if (remaining_segments >= 2 * (N - i - 1) and 
                    remaining_segments <= 7 * (N - i - 1)):
                    # Update the sum and add the current digit to the answer
                    total_segments -= f[j]
                    ans += str(j)
                    break

        # Return the resulting digits as a string
        return ans
