def distinctColoring(N, r, g, b):
    # Base case for the first house
    dp_red = r[0]  # Cost of painting the first house red
    dp_green = g[0]  # Cost of painting the first house green
    dp_blue = b[0]  # Cost of painting the first house blue
    
    # Iterate through the remaining houses
    for i in range(1, N):
        # Calculate the cost for each color for house i
        new_red = r[i] + min(dp_green, dp_blue)  # Red cost for current house
        new_green = g[i] + min(dp_red, dp_blue)  # Green cost for current house
        new_blue = b[i] + min(dp_red, dp_green)  # Blue cost for current house
        
        # Update the DP variables for the next iteration
        dp_red, dp_green, dp_blue = new_red, new_green, new_blue
    
    # The final answer will be the minimum cost of the last house being any color
    return min(dp_red, dp_green, dp_blue)

# Example usage:
N = 3
r = [1, 1, 1]
g = [2, 2, 2]
b = [3, 3, 3]
print(distinctColoring(N, r, g, b))  # Output: 4

N = 3
r = [2, 1, 3]
g = [3, 2, 1]
b = [1, 3, 2]
print(distinctColoring(N, r, g, b))  # Output: 3
