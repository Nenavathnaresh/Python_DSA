#print(10)
#Lambda functions
'''def sum(a,b):
    print(a+b)
sum(3,6)'''

'''x = lambda a,b : a+b
print(x(5,3))'''

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
'''for i in people:
    print(i['age'])
print(people[0])'''

'''def age(d):
    return d['age']
people.sort(key=age)
print(people)
'''
'''people.sort(key=lambda s: s['age'],reverse=True)
print(people)'''

#map method;
num = [1,2,3,4,5,]
'''squares = [x**2 for x in num]
print(squares)'''
'''sq = map(lambda a : a**2,num)
print(dict(sq))'''

even = filter(lambda a:a%2==0,num)
print(list(even))