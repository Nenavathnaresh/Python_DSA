def countDistinctIslands(grid):
    def dfs(x, y, base_x, base_y):
        if (x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0):
            return
        
        # Mark the cell as visited
        grid[x][y] = 0
        shape.append((x - base_x, y - base_y))  # Store the relative position
        
        # Explore all 4 possible directions
        dfs(x + 1, y, base_x, base_y)
        dfs(x - 1, y, base_x, base_y)
        dfs(x, y + 1, base_x, base_y)
        dfs(x, y - 1, base_x, base_y)
    
    n, m = len(grid), len(grid[0])
    unique_islands = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                shape = []
                dfs(i, j, i, j)
                # Add the shape to the set of unique shapes
                unique_islands.add(tuple(shape))
    
    return len(unique_islands)

# Example Test Cases
grid1 = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]]

grid2 = [[1, 1, 0, 1, 1],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 1, 1]]

print(countDistinctIslands(grid1))  # Output: 1
print(countDistinctIslands(grid2))  # Output: 3
