# sequence data type 

# ordered, unchangable, allow duplicates

# t1 = (1,2,3,4)  # data can not be modified
# print(t1[-1])
# print(t1[1])
# print(t1[0])
# print(t1[2])

t2 = 32,54,74 # this will be stored as (32,54,74)
# print(t2)
t3 = (56, 'hello') # heterogenious

k = []
t4 = ()
t5 = (67,) # if need one value in tuple put , after the element or else it will consider as variable

t6 = 23, 'hello',[1,2] # tuple packing 
# print(t6[-1][0])

# t6[1] = 'naresh'  -----> tuple are immutable list are mutable
# print(t6)

# a,b,c = t6  -----> unpacking ----> if values are less or many it give us an error
# print(a)
# print(b)
# # print(c)
# arr = [4,2,6,3,6,3,45]
# for t in enumerate(arr):  # o/p tuple 
#     print(t)
# for i,v in enumerate(arr):  ----> tuple unpacking
#     print(i)
#     print(v)


