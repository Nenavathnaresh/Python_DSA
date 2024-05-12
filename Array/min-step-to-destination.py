def minstep(d):
    steps = 0
    distance = 0
    while distance < d or (distance - d) % 2 != 0:
        steps += 1 
        distance += steps 
    return steps 
print(minstep(2))
print(minstep(10))