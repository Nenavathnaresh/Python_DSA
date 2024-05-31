def findPlatform(arr, dep, n):
    # Sort arrival and departure times
    arr.sort()
    dep.sort()
    
    # Initialize pointers for arrival and departure arrays
    i = 0
    j = 0
    
    # Initialize current number of platforms needed and the result (max platforms needed)
    platforms_needed = 0
    max_platforms = 0
    
    # Traverse arrival and departure arrays
    while i < n and j < n:
        # If next event is arrival, increment platforms_needed
        if arr[i] <= dep[j]:
            platforms_needed += 1
            i += 1
        # If next event is departure, decrement platforms_needed
        else:
            platforms_needed -= 1
            j += 1
        
        # Update the result if needed
        max_platforms = max(max_platforms, platforms_needed)
    
    return max_platforms

# Example usage:
arr1 = [900, 940, 950, 1100, 1500, 1800]
dep1 = [910, 1200, 1120, 1130, 1900, 2000]
n1 = 6
print(findPlatform(arr1, dep1, n1))  # Output: 3

arr2 = [900, 1100, 1235]
dep2 = [1000, 1200, 1240]
n2 = 3
print(findPlatform(arr2, dep2, n2))  # Output: 1
