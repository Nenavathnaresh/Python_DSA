def mergeIntervals(arr):
    # Sort intervals by start time
    arr.sort(key=lambda x: x[0])
    
    # Initialize result list
    merged = []
    
    for interval in arr:
        # If the merged list is empty or no overlap, add the current interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Overlapping intervals: merge by updating the end time
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example Usage
arr1 = [[1, 3], [2, 4], [6, 8], [9, 10]]
arr2 = [[6, 8], [1, 9], [2, 4], [4, 7]]

print(mergeIntervals(arr1))  # Output: [[1, 4], [6, 8], [9, 10]]
print(mergeIntervals(arr2))  # Output: [[1, 9]]
