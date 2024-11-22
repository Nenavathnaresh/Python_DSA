num = 12345
reversed_num = int(str(num)[::-1])
print(reversed_num)  # Output: 54321


################

num = 12345
reversed_num = 0

while num > 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit
    num = num // 10  # Remove the last digit

print(reversed_num)  # Output: 54321

#########################

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    return reverse_num(num // 10, rev * 10 + num % 10)

num = 12345
reversed_num = reverse_num(num)
print(reversed_num)  # Output: 54321


#####################

num = 12345
reversed_num = int("".join(reversed(str(num))))
print(reversed_num)  # Output: 54321

########################

num = 12345
stack = list(str(num))
reversed_num = int("".join(stack[::-1]))
print(reversed_num)  # Output: 54321

#########################

num = 12345
reversed_num = 0
while num:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print(reversed_num)  # Output: 54321


####################

from functools import reduce

num = 12345
reversed_num = reduce(lambda acc, x: acc * 10 + int(x), str(num), 0)
print(reversed_num)  # Output: 54321


###########################

num = 12345
reversed_num = int("".join(str(num)[i] for i in range(len(str(num)) - 1, -1, -1)))
print(reversed_num)  # Output: 54321



