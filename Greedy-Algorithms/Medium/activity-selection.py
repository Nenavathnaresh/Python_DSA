def activityselection(start, end, N):
    # Create a list of activities with start and end times
    activities = list(zip(start, end))
    
    # Sort activities based on their end times
    activities.sort(key=lambda x: x[1])
    
    # The end time of the last selected activity
    last_end_time = 0
    count = 0
    
    # Iterate over the sorted activities
    for i in range(N):
        if activities[i][0] >= last_end_time:
            # If the start time of the current activity is greater than or equal
            # to the end time of the last selected activity, select this activity
            count += 1
            last_end_time = activities[i][1]
    
    return count

# Example usage:
start1 = [2, 1]
end1 = [2, 2]
N1 = 2
print(activityselection(start1, end1, N1))  # Output: 1

start2 = [1, 3, 2, 5]
end2 = [2, 4, 3, 6]
N2 = 4
print(activityselection(start2, end2, N2))  # Output: 3
