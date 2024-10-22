def countSubarrays(arr, x, y):
    # Dictionary to store the frequency of difference (count(x) - count(y))
    count_map = {0: 1}  # Initially, we have one subarray with a diff of 0 (empty subarray)
    diff = 0  # Tracks the difference between counts of x and y
    result = 0  # Store the result

    # Traverse through the array
    for num in arr:
        # Update the difference based on the current element
        if num == x:
            diff += 1
        elif num == y:
            diff -= 1
        
        # If the current difference has been seen before, it means there are
        # subarrays ending at the current index where the counts of x and y are equal.
        if diff in count_map:
            result += count_map[diff]
        
        # Update the map with the current difference
        count_map[diff] = count_map.get(diff, 0) + 1

    return result

# Example usage:
arr = [1, 2, 1]
x = 1
y = 2
print(countSubarrays(arr, x, y))  # Output: 2

arr = [1, 2, 1]
x = 4
y = 6
print(countSubarrays(arr, x, y))  # Output: 6

arr = [1, 2, 1]
x = 1
y = 4
print(countSubarrays(arr, x, y))  # Output: 1
