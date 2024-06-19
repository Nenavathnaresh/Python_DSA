import math

class Solution:
    def maxVolume(self, perimeter, area):
        #code here
        p1 = perimeter - math.sqrt(perimeter**2 - (24*area))
        term = (p1/12)**2
        h = (perimeter/4) - (2*(p1/12))
        ans = term * h 
        return ans
    
    print(maxVolume(22, 15))  # Expected output: 3.02
    print(maxVolume(20, 5))   # Expected output: 0.33