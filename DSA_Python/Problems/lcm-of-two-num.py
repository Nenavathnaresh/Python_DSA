################### method 1 using gcd ##########################
import math
def lcm(n,m):
    return abs(n*m) // math.gcd(n,m)

print(lcm(3,4))

#################### method 2  using loop ##########################

def lcmUsingLoop(m,n):
    lcm = max(m,n)

    while True:
        if lcm % m == 0 and lcm % n == 0:
            return lcm 
        lcm += 1 
print(lcmUsingLoop(3,4))