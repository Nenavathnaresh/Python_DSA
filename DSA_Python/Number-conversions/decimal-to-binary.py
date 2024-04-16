
# 1. Decimal to Binary

# a.Manually implementing the conversions

def  deciToBinary(deci_num):
    binary = ''
    if deci_num == 0 :
        return 0 
    while deci_num > 0:
        remainder = deci_num % 2 
        binary = str(remainder) + binary
        deci_num = deci_num // 2 
    return binary 

x = deciToBinary(10)
print(x)

# b. By using bin() function

deci = 10 
binary = bin(deci)
print(f"the binary of {deci} is {binary}")

#2. Binary to Decimal 
   #a. using int function:

binaryNumber = '10101'
decimalNumber = int(binaryNumber,2)
print(decimalNumber)

#b.Manually implementing the conversions :

def BiToDeci(Bi):
    deci = 0 
    power = len(Bi)-1
    for digit in Bi :
        deci += int(digit) * (2**power)
        power -= 1 
    return deci
x = BiToDeci('10101')
print(x)

