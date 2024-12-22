def aggressiveCows(stalls, k):
    def canPlaceCows(min_dist):
        count = 1  # Place the first cow in the first stall
        last_position = stalls[0]
        
        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= min_dist:
                count += 1
                last_position = stalls[i]
                if count == k:
                    return True
        return False

    stalls.sort()  # Sort the stall positions
    low, high = 1, stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if canPlaceCows(mid):
            result = mid  # Update result
            low = mid + 1  # Try for a larger minimum distance
        else:
            high = mid - 1  # Try for a smaller minimum distance

    return result

# Example Usage
print(aggressiveCows([1, 2, 4, 8, 9], 3))  # Output: 3
print(aggressiveCows([10, 1, 2, 7, 5], 3))  # Output: 4
print(aggressiveCows([2, 12, 11, 3, 26, 7], 5))  # Output: 1
