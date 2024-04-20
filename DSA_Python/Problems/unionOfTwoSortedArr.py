# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& Union of two sorted array &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined 
# as the common and distinct elements in the two arrays.

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,6,7]
n = len(arr1)
m = len(arr2)

def findUnion(arr1, arr2, n, m):
    unionDict = {}
    res = []
    for num in arr1:
        if num in unionDict:
            unionDict[num] += 1 
        else:
            unionDict[num] = 1 
            res.append(num)
    for num in arr2:
        if num in unionDict:
            unionDict[num] += 1 
        else:
            unionDict[num] = 1 
            res.append(num)
    res.sort()
    return res 

res = findUnion(arr1, arr2, n, m)
print(res)

# %%%%%%%%%%%%% Without using the sort function %%%%%%%%%%%%%%%%%%%%%%%%%

def union(arr1, arr2, n, m):
    i = j = 0
    res = []
    while i < n and j < m:
        if arr1[i] < arr2[j] :
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1 
        elif arr1[i] > arr2[j] :
            if not res or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1 
        else:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1 
            j += 1 
    while i < n:
        if not res or res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1 
    while j < m:
        if not res or res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1 
    return res
result = union(arr1, arr2, n, m)
print(result)



