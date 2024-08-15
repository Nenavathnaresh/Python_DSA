def dfs(grid, visited, i, j, n, m):
    # Direction vectors for up, down, left, and right movements
    direction_x = [-1, 1, 0, 0]
    direction_y = [0, 0, -1, 1]
    
    # Mark the current cell as visited
    visited[i][j] = True
    
    # Explore the 4 possible directions
    for d in range(4):
        new_i, new_j = i + direction_x[d], j + direction_y[d]
        
        if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 'X' and not visited[new_i][new_j]:
            dfs(grid, visited, new_i, new_j, n, m)

def xShape(grid):
    n = len(grid)    # Number of rows
    m = len(grid[0]) # Number of columns
    
    # Visited array to mark visited cells
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    shape_count = 0
    
    # Traverse each cell in the grid
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X' and not visited[i][j]:
                # Start a new DFS if an unvisited 'X' is found
                dfs(grid, visited, i, j, n, m)
                shape_count += 1
    
    return shape_count

# Example usage:
grid1 = [['X', 'O', 'X'], 
         ['O', 'X', 'O'], 
         ['X', 'X', 'X']]

grid2 = [['X', 'X'], 
         ['X', 'X']]

print(xShape(grid1))  # Output: 3
print(xShape(grid2))  # Output: 1
