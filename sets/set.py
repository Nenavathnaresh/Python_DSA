# unordered, unchangable, do not allow duplicates 
a = set() #empty set 
# b = {'apple','banana','orange','cherry','pear'}
# print('apple' in b)
# print(b[0]) ----> error unordered 

# fruits = ['apple','banana','orange','cherry','pear']
# print('apple' in fruits)

# c = set(fruits)
# print(c)

# d = set('banana')
# print(d)

fruits = ['apple','grapes','pear','orange','banana']
greenFruits = ['grapes','pear','kiwi']
f = set(fruits)
g = set(greenFruits)
print(f)
print(g)

# <-------difference -------->

# print(f-g) # which are there in f but not in g
# print(g-f) # which are there in g but not in f

# print(f|g) # both in f or g means all fruits

# print(f & g) # should present in both f and g 

# print(f ^ g) # which are there in only one of them either g or f



