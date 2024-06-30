def floodFill(image, sr, sc, newColor):
    # Get the dimensions of the image
    n = len(image)
    m = len(image[0])
    
    # Get the initial color of the starting pixel
    originalColor = image[sr][sc]
    
    # If the new color is the same as the original color, no need to change anything
    if originalColor == newColor:
        return image
    
    def dfs(r, c):
        # Base case: if out of bounds or the color is not the same as the original color, return
        if r < 0 or r >= n or c < 0 or c >= m or image[r][c] != originalColor:
            return
        
        # Change the color to the new color
        image[r][c] = newColor
        
        # Recursively call dfs for 4-directionally connected pixels
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
    
    # Start the DFS from the given starting pixel
    dfs(sr, sc)
    
    return image

# Example usage:
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr = 1
sc = 1
newColor = 2

result = floodFill(image, sr, sc, newColor)
print(result)  # Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
