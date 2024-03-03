num = int(input('enter a num '))
x = int(input('enter a num '))

if(x > num):
    print('not valid input')
else:
    if(x == 0):
        print('can not divide a num by zero')
    if(num % x == 0):
        print(f'{x} is a factor of {num}')
    else:
        print(f'{x} is not a factore of {num}')