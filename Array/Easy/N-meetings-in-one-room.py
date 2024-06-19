def maxMeetings(N, start, end):
    # Pair up start and end times and sort by end times
    meetings = sorted(zip(start, end), key=lambda x: x[1])
    
    # Initialize the count of meetings and the end time of the last meeting
    count = 0
    last_end_time = -1
    
    # Iterate through the sorted meetings
    for s, e in meetings:
        # If the current meeting starts after the last meeting ends, select it
        if s > last_end_time:
            count += 1
            last_end_time = e
    
    return count

# Test cases
print(maxMeetings(6, [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))  # Output: 4
print(maxMeetings(3, [10, 12, 20], [20, 25, 30]))  # Output: 1
