
import sys
from typing import List
sys.setrecursionlimit(10**8)

#recursive function to perform depth-first search
def dfs(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return
    
    #mark the current cell as visited (0)
    grid[i][j] = 0
    dfs(i + 1, j, grid)
    dfs(i, j + 1, grid)
    dfs(i, j - 1, grid)
    dfs(i - 1, j, grid)

class Solution:
    #function to calculate the number of enclaves
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        #perform DFS on boundary cells
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1 and grid[i][j] == 1:
                    dfs(i, j, grid)
        
        #count the remaining enclaves
        count = 0
        for i in range(n):
            for j in range(m):
                count += grid[i][j]

        return count
    
    #########################################################################################################

def numberOfEnclaves(grid):
    def dfs(x, y):
        # If the cell is out of bounds or it's a sea cell, stop the DFS
        if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == 0:
            return
        # Mark the cell as visited by setting it to 0
        grid[x][y] = 0
        # Explore all 4 possible directions
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    n, m = len(grid), len(grid[0])
    
    # Run DFS for all boundary cells that are land cells
    for i in range(n):
        if grid[i][0] == 1:
            dfs(i, 0)
        if grid[i][m-1] == 1:
            dfs(i, m-1)
    
    for j in range(m):
        if grid[0][j] == 1:
            dfs(0, j)
        if grid[n-1][j] == 1:
            dfs(n-1, j)
    
    # Count the remaining land cells that are not connected to the boundary
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count += 1
    
    return count

# Example Test Cases
grid1 = [[0, 0, 0, 0],
         [1, 0, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]]

grid2 = [[0, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 1],
         [0, 1, 1, 0]]

print(numberOfEnclaves(grid1))  # Output: 3
print(numberOfEnclaves(grid2))  # Output: 4
