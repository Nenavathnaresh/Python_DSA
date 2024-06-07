def maxOccurringInteger(n, l, r, maxx):
    # Create a count array to store the range counts
    count = [0] * (maxx + 2)
    
    # Update the count array using the ranges
    for i in range(n):
        count[l[i]] += 1
        if r[i] + 1 <= maxx:
            count[r[i] + 1] -= 1
    
    # Calculate prefix sums to find the number of ranges covering each integer
    max_count = 0
    max_occurring_integer = 0
    current_count = 0
    
    for i in range(maxx + 1):
        current_count += count[i]
        if current_count > max_count:
            max_count = current_count
            max_occurring_integer = i
    
    return max_occurring_integer

# Example usage
n = 4
l = [1, 4, 3, 1]
r = [15, 8, 5, 4]
maxx = 15
print(maxOccurringInteger(n, l, r, maxx))  # Output: 4

n = 5
l = [1, 5, 9, 13, 21]
r = [15, 8, 12, 20, 30]
maxx = 30
print(maxOccurringInteger(n, l, r, maxx))  # Output: 5
