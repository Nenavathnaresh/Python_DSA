def countSmaller(arr):
    n = len(arr)
    result = [0] * n
    indices = list(range(n))

    def mergeSort(left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mergeSort(left, mid)
        mergeSort(mid + 1, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        temp = []
        l = left
        r = mid + 1
        right_count = 0

        while l <= mid and r <= right:
            if arr[indices[r]] < arr[indices[l]]:
                right_count += 1
                temp.append(indices[r])
                r += 1
            else:
                result[indices[l]] += right_count
                temp.append(indices[l])
                l += 1

        while l <= mid:
            result[indices[l]] += right_count
            temp.append(indices[l])
            l += 1

        while r <= right:
            temp.append(indices[r])
            r += 1

        for i in range(left, right + 1):
            indices[i] = temp[i - left]

    mergeSort(0, n - 1)
    return result

# Example usage:
arr1 = [12, 1, 2, 3, 0, 11, 4]
print(countSmaller(arr1))  # Output: [6, 1, 1, 1, 0, 1, 0]

arr2 = [1, 2, 3, 4, 5]
print(countSmaller(arr2))  # Output: [0, 0, 0, 0, 0]
