# print(list(range(5)))
# f = list('hello')
# f = list((1,2))
# print(list({'firstname':'naresh'}))
# print(f)

# k = sorted(range(5))

# li = [1,2,3,4,5]
# # li.sort(reverse=True)
# j = reversed(li)
# print(list(j))

# <---------list comprehence ------->
# li = [12,4,3,5,2]
# l1 = [x*2 for x in li]
# print(l1)

# l3 = [1,2,3,4,5]
# # sq = [x**2 for x in l3]
# sq = [x**3 for x in range(5)]
# print(sq)

# <-------set com ------>
# s1 = {x for x in 'apple' if x not in 'banana'}
# print(s1)

# #<----dict com----->
# sq = {x:x**2 for x in range(1,6)}
# print(sq)

#<------zip------>
# keys = ['first','last','age']
# val = ['naresh','nenavath','20']
# for k,v in zip(keys,val):
#     print('the {0} is {1}'.format(k,v))

people = [
                            {
                            "firstname": "praveen",
                            "lastname": "gubbala",
                            "age": 36,
                            "gender": "male",
                            "city": "hyd",
                            "salary": 10000
                            },
                            {
                            "firstname": "srikanth",
                            "lastname": "gubbala",
                            "age": 32,
                            "gender": "male",
                            "city": "bengaluru",
                            "salary": 20000
                            },
                            {
                            "firstname": "pradeep",
                            "lastname": "reddy",
                            "age": 21,
                            "gender": "male",
                            "city": "hyd",
                            "salary": 25000
                            },
                            {
                            "firstname": "mounika",
                            "lastname": "mudiraj",
                            "age": 20,
                            "gender": "female",
                            "city": "nalgonda",
                            "salary": 30000
                            },
                            {
                            "firstname": "nikhil",
                            "lastname": "m",
                            "age": 22,
                            "gender": "male",
                            "city": "guntur",
                            "salary": 2000
                            },
                            {
                            "firstname": "riya",
                            "lastname": "bhadouria",
                            "age": 14,
                            "gender": "female",
                            "city": "indore",
                            "salary": 40000
                            }
                            ]
# people.sort() ----> Error
def sal(d):
    return d['salary']
def age(d):
    return d['age']
def fn(d):
    return d['firstname']
# people.sort(key = sal, reverse=True)
# people.sort(key = age)
# people.sort(key = fn)
# print(people)


# <------Lambda ------>

# y = lambda x : x+5
# print(y(5))

# people.sort(key = lambda x:x['salary'])
# people.sort(key = lambda x: x['firstname'])
print(people)
