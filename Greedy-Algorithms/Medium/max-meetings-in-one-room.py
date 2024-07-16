def maxMeetings(S, F, N):
    # Pair up the start and finish times with their original index
    meetings = [(S[i], F[i], i+1) for i in range(N)]
    
    # Sort the meetings based on finish time. If finish times are the same, sort by start time
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    # List to store the indices of the selected meetings
    selected_meetings = []
    
    # Initialize the end time of the last selected meeting
    last_end_time = 0
    
    # Iterate through the sorted list of meetings
    for start, finish, index in meetings:
        if start > last_end_time:
            # If the meeting can be accommodated, select it
            selected_meetings.append(index)
            last_end_time = finish
    
    # Return the list of selected meeting indices in sorted order
    return sorted(selected_meetings)

# Example usage:
N = 10
S = [12, 6, 16, 12, 6, 9, 16, 6, 17, 5]
F = [17, 13, 16, 18, 17, 10, 18, 12, 18, 11]
print(maxMeetings(S, F, N))  # Output: [3, 6, 9]
