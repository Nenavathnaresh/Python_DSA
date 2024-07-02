import math

def next_gap(gap):
    if gap <= 1:
        return 0
    return math.ceil(gap / 2)

def merge(arr1, arr2, n, m):
    gap = n + m
    gap = next_gap(gap)
    
    while gap > 0:
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        j = max(0, gap - n)
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        gap = next_gap(gap)

# Example usage:
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
merge(arr1, arr2, len(arr1), len(arr2))
print("arr1:", arr1)  # Output: [0, 1, 2, 3]
print("arr2:", arr2)  # Output: [5, 6, 7, 8, 9]

arr1 = [10, 12]
arr2 = [5, 18, 20]
merge(arr1, arr2, len(arr1), len(arr2))
print("arr1:", arr1)  # Output: [5, 10]
print("arr2:", arr2)  # Output: [12, 18, 20]
