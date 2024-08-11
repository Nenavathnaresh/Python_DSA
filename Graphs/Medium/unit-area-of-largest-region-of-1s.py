def findMaxArea(grid):
    def dfs(x, y):
        # Directions array for 8 possible moves (8-directional)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        stack = [(x, y)]
        area = 0
        
        while stack:
            x, y = stack.pop()
            
            # If out of bounds or the cell is not 1, continue
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
                continue
                
            # Mark the cell as visited by setting it to 0
            grid[x][y] = 0
            area += 1
            
            # Push all 8 neighbors to the stack
            for dx, dy in directions:
                stack.append((x + dx, y + dy))
        
        return area

    n = len(grid)
    m = len(grid[0])
    max_area = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # Perform DFS and get the area of the region
                area = dfs(i, j)
                # Update the maximum area found
                max_area = max(max_area, area)
    
    return max_area

# Example Usage:
grid1 = [[1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
grid2 = [[0, 1]]
print(findMaxArea(grid1))  # Output: 5
print(findMaxArea(grid2))  # Output: 1
