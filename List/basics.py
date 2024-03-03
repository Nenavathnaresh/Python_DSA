# number - int/float 
# string - str 
# boolean - bool 

# sequence data type / mapping data type ---> store more then one value at a time 
# combined together are known as iterables

# sequence data type --->Lists, string, tuple 
# mapping data type ---> dict 


# why str is sequence data type ..? ----> as we are able to access the values by index and we can loop then so they are called sdt
# s = 'hello'
# s = 'well come'
# print(s)
# print(s[2])
# print(s[5])
# for a in s :
#     print(a)

# Lists......>

num = [1,2,3,4,6,6] #homogenious list 
# names = ['naresh', 'suresh', 'divya', 'shy'] # homogenious list
# mylist = ['naresh', 24,252,True, 'well come',[1,2,3]] # heterogenious list
# print(num[3])
# print(len(num))
# print(num[1:4])
# a = 'hello'
# a[1] = 'u' ----> #wont support because str are immutable cant be changed but replaced
# print(a)
# num[1] = 101 
# print(num)
evenNums = [2,4,6,8]
oddNums = [1,3,5,7]
# allNums = evenNums + oddNums 

# looping......

allNums = [2,4,6,8,1,3,5,7,9] 
n = len(allNums)
# for x in allNums:
#     print(x)
# for i in range(len(allNums)):
#     # print(i)
#     print(i,allNums[i])
# for a in enumerate(allNums):
#     print(a)
# for a,b in enumerate(allNums):
#     print(a)
#     print(b)

# # print all values from last to first 
# for i in range(n-1,-1,-1):
#     print(allNums[i])
# print(allNums[n:0:-1])


# enumarate----->

# for a in enumerate(allNums): # o/p ---> tuple
    # print(a)

# for i,v in enumerate(allNums):
    # print(i,v)


