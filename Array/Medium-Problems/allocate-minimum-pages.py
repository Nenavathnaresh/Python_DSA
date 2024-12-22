def isValid(arr, n, k, maxPages):
    students = 1
    pages_allocated = 0

    for pages in arr:
        if pages > maxPages:
            return False  # Single book exceeds maxPages
        if pages_allocated + pages > maxPages:
            students += 1
            pages_allocated = pages
            if students > k:
                return False
        else:
            pages_allocated += pages

    return True

def findMinPages(arr, k):
    n = len(arr)
    if k > n:  # Not enough books for all students
        return -1

    low, high = max(arr), sum(arr)
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if isValid(arr, n, k, mid):
            result = mid
            high = mid - 1  # Minimize the maximum pages
        else:
            low = mid + 1

    return result

# Example Usage
print(findMinPages([12, 34, 67, 90], 2))  # Output: 113
print(findMinPages([15, 17, 20], 5))      # Output: -1
print(findMinPages([22, 23, 67], 1))      # Output: 112
