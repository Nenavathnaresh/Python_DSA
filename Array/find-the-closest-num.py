def findClosest(n,k,arr):
    minDiff = float("inf")
    for i in range(n):
        diff = abs(k-arr[i])
        if diff < minDiff:
            minDiff = diff 
            ind = i 
    return arr[ind]

n=4
k=4
arr = [1,3,6,7]
print(findClosest(n,k,arr))