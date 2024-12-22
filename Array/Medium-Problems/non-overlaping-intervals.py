def erase_overlap_intervals(intervals):
    # Step 1: Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    
    # Step 2: Initialize variables
    end = float('-inf')  # Represents the end of the last included interval
    removals = 0         # Count of intervals to remove
    
    # Step 3: Traverse the intervals
    for start, finish in intervals:
        if start < end:
            # Overlapping interval, increase removals
            removals += 1
        else:
            # Non-overlapping, update the end time
            end = finish
    
    return removals

# Example Usage
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(erase_overlap_intervals(intervals))  # Output: 1

intervals = [[1, 3], [1, 3], [1, 3]]
print(erase_overlap_intervals(intervals))  # Output: 2

intervals = [[1, 2], [5, 10], [18, 35], [40, 45]]
print(erase_overlap_intervals(intervals))  # Output: 0
