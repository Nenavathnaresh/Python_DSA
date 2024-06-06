def findAllPossiblePaths(n, m, grid):
    def findPaths(x, y, path, result):
        # Check if current position is out of bounds
        if x >= n or y >= m:
            return
        
        # Append the current cell to the path
        path.append(grid[x][y])
        
        # If we have reached the bottom-right corner, add the path to result
        if x == n - 1 and y == m - 1:
            result.append(path.copy())
        else:
            # Move right
            findPaths(x, y + 1, path, result)
            # Move down
            findPaths(x + 1, y, path, result)
        
        # Backtrack: remove the last cell from the path
        path.pop()

    result = []
    findPaths(0, 0, [], result)
    return result

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from typing import List
class Solution:
    def calculate(self,n,m,i,j,ans,temp,grid):
        if(i>=n or j>=m): return 
        
        temp.append(grid[i][j])
        
        if(i==n-1 and j == m-1):
            ans.append(temp[:])
        
        self.calculate(n,m,i+1,j,ans,temp,grid)
        self.calculate(n,m,i,j+1,ans,temp,grid)
        temp.pop()
    def findAllPossiblePaths(self, n : int, m : int, grid : List[List[int]]) -> List[List[int]]:
        ans = []
        temp = []
        self.calculate(n,m,0,0,ans,temp,grid)
        return ans


# Example 1
n = 2
m = 3
grid = [
    [1, 2, 3],
    [4, 5, 6]
]
print(findAllPossiblePaths(n, m, grid))
# Output: [[1, 2, 3, 6], [1, 2, 5, 6], [1, 4, 5, 6]]

# Example 2
n = 2
m = 2
grid = [
    [1, 2],
    [3, 4]
]
print(findAllPossiblePaths(n, m, grid))
# Output: [[1, 2, 4], [1, 3, 4]]
