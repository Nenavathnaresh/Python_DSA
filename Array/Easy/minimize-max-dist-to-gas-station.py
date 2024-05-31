def findSmallestMaxDist(stations, K):
    import math
    left, right = 1e-6, stations[-1] - stations[0]
    while left + 1e-6 < right:
        mid = (left + right) / 2
        count = 0

            # Counting the number of stations that can be added with the current maximum distance
        for a, b in zip(stations, stations[1:]):
            print(a)
            count += math.ceil((b - a) / mid) - 1

            # Updating the left or right values based on the count
        if count > K:
            left = mid
        else:
            right = mid
    return right

# Example usage:
stations1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1 = 9
print(findSmallestMaxDist(stations1, k1))  # Output: 0.50

# stations2 = [3, 6, 12, 19, 33, 44, 67, 72, 89, 95]
# k2 = 2
# print(findSmallestMaxDist(stations2, k2))  # Output: 14.00
