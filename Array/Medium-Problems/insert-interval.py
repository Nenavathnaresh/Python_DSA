class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        intervals.append(newInterval)
        
        intervals.sort(key = lambda x : x[0])
        res = []
        
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
    

###############################

def insert_interval(intervals, newInterval):
    result = []
    i = 0

    # Traverse all intervals
    while i < len(intervals):
        # Case 1: Interval ends before newInterval starts
        if intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
        # Case 2: Interval starts after newInterval ends
        elif intervals[i][0] > newInterval[1]:
            result.append(newInterval)  # Add the new interval
            newInterval = intervals[i]  # Replace it with the current interval
        # Case 3: Overlapping intervals
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add the remaining newInterval
    result.append(newInterval)
    return result

# Example Usage
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 9]
print(insert_interval(intervals, newInterval))  # Output: [[1, 2], [3, 10], [12, 16]]


####################################


def insertInterval(intervals, newInterval):
    result = []
    newStart, newEnd = newInterval
    added = False

    for start, end in intervals:
        # If the current interval ends before the new interval starts
        if end < newStart:
            result.append([start, end])
        # If the current interval starts after the new interval ends
        elif start > newEnd:
            if not added:
                result.append([newStart, newEnd])
                added = True
            result.append([start, end])
        # If the current interval overlaps with the new interval
        else:
            newStart = min(newStart, start)
            newEnd = max(newEnd, end)

    # If the new interval hasn't been added yet, add it
    if not added:
        result.append([newStart, newEnd])

    return result

# Example Usage
print(insertInterval([[1,3], [4,5], [6,7], [8,10]], [5,6]))  # Output: [[1,3], [4,7], [8,10]]
print(insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]))  # Output: [[1,2], [3,10], [12,16]]
