def findMedianSum(arr1, arr2):
    n = len(arr1)
    if n == 0:
        return 0

    if n > len(arr2):
        arr1, arr2 = arr2, arr1  # Ensure arr1 is the smaller array
    x, y = len(arr1), len(arr2)

    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxX = float('-inf') if partitionX == 0 else arr1[partitionX - 1]
        maxY = float('-inf') if partitionY == 0 else arr2[partitionY - 1]

        minX = float('inf') if partitionX == x else arr1[partitionX]
        minY = float('inf') if partitionY == y else arr2[partitionY]

        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return max(maxX, maxY) + min(minX, minY)
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted")

# Example usage:
arr1 = [1, 2, 4, 6, 10]
arr2 = [4, 5, 6, 9, 12]
print(findMedianSum(arr1, arr2))  # Output: 11

arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]
print(findMedianSum(arr1, arr2))  # Output: 32
