# mapping data types 
# unordered changable allow duplicates 

person = {
    'firstname':'naresh',    # key - value pairs 
    'lastname':'nenavath',
    'age':23
}
person2 = {
    'firstname':'naresh',
    'lastname':'nenavath',
    'age':23
}

# # print(person)
# print(person['firstname'])
# print(person['lastname'])
# print(person['age'])
# print(person.age)  -----> error

# person["firstname"] = 'Suresh'
# person['city'] = 'Hyderabad'
# del person['city']

# li = list(person) # -----> keys will be printed 
# li = sorted(person) # ------> keys are sorted in assending order
# print(li)

# print("naresh" in person)  ----> false checks only in keys

# dict constuctore ---->
# p = dict([('firstname',"suresh"),("last","nenavath"),("age",34)])
# print(p)
# p = dict(firstname='suresh',lastname='naresh',age=34)
# print(p)

# Looping.......>
# print(person.items())
# for kv in person.items(): ----> in tuple key and values
#     print(kv)

# for k,v in person.items():
    # print(k)  ------> o/p keys
    # print(v)   ------> o/p values

# for k in person.values():  ----> o/p values
#     print(k)

# for k in person.keys():   ----->o/p keys
    # print(k)