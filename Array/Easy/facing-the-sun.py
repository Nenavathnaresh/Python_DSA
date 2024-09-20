def countBuildings(height):
    # Initialize count of buildings that can see the sunrise
    count = 1  # The first building always sees the sunrise
    
    # Initialize the maximum height with the first building
    max_height = height[0]
    
    # Traverse the array starting from the second building
    for i in range(1, len(height)):
        if height[i] > max_height:
            # If the current building is taller than the previous max, it can see the sunrise
            count += 1
            max_height = height[i]  # Update the max height
    
    return count

# Example usage:
height1 = [7, 4, 8, 2, 9]
print(countBuildings(height1))  # Output: 3

height2 = [2, 3, 4, 5]
print(countBuildings(height2))  # Output: 4
