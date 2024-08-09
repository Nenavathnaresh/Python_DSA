from collections import deque

def isPathPossible(grid):
    n = len(grid)
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Find source (1) and destination (2)
    source = None
    destination = None
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                source = (i, j)
            elif grid[i][j] == 2:
                destination = (i, j)
    
    if not source or not destination:
        return 0
    
    # BFS setup
    queue = deque([source])
    visited = [[False] * n for _ in range(n)]
    visited[source[0]][source[1]] = True
    
    # BFS Loop
    while queue:
        x, y = queue.popleft()
        
        # Check if we've reached the destination
        if (x, y) == destination:
            return 1
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return 0

# Example test cases
grid1 = [
    [3, 0, 3, 0, 0],
    [3, 0, 0, 0, 3],
    [3, 3, 3, 3, 3],
    [0, 2, 3, 0, 0],
    [3, 0, 0, 1, 3]
]
print(isPathPossible(grid1))  # Output: 0

grid2 = [
    [1, 3],
    [3, 2]
]
print(isPathPossible(grid2))  # Output: 1
