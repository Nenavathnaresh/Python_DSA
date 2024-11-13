def canAttendAllMeetings(arr):
    # Sort meetings by their starting times
    arr.sort(key=lambda x: x[0])
    
    # Iterate through sorted meetings to check for any overlap
    for i in range(1, len(arr)):
        # If the start time of the current meeting is less than
        # the end time of the previous meeting, return False
        if arr[i][0] < arr[i - 1][1]:
            return False
    
    # If no overlaps were found, return True
    return True
