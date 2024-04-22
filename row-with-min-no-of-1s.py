def minRow(m,n,a):
    minCount = float("inf")
    for i in range(n):
        count = 0
        for j in range(m):
            if a[i][j] == 1 :
                count += 1 
        if count < minCount:
            minCount = count 
            index = i + 1 
    return index 

n = 4
m = 4
a = [[1, 1, 1, 1],
     [1, 1, 0, 0], 
     [0, 0, 1, 1],
     [1, 1, 1, 1]]
x = minRow(n,m,a)
print(x)
