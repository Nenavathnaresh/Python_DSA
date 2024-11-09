def splitArrayIntoThreeEqualParts(arr):
    total_sum = sum(arr)
    
    # If the total sum is not divisible by 3, we can't split it as required
    if total_sum % 3 != 0:
        return [-1, -1]
    
    target_sum = total_sum // 3
    n = len(arr)
    
    # Initialize cumulative sum and counters for the first and second parts
    cumulative_sum = 0
    first_index = -1
    second_index = -1
    part_count = 0
    
    for index in range(n):
        cumulative_sum += arr[index]
        
        # When we reach the target sum for a part
        if cumulative_sum == target_sum:
            part_count += 1
            if part_count == 1:
                first_index = index
            elif part_count == 2:
                second_index = index
                break
            # Reset cumulative sum for the next part
            cumulative_sum = 0

    # If we found both indices for the first and second parts, return them
    if part_count == 2 and second_index != -1:
        return [first_index, second_index]
    
    return [-1, -1]
