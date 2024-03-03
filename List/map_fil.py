nums = [1,2,3,4,5,67,5]
# sq = [x**2 for x in nums]
# print(sq)


s = map(lambda x:x**2, nums)
print(list(s))

t = filter(lambda x: x%2==1, nums)
print(list(t))