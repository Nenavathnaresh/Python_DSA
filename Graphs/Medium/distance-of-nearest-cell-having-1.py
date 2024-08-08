from collections import deque

def nearest(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Initialize the distance matrix with infinity
    dist = [[float('inf')] * m for _ in range(n)]
    
    # Queue for BFS
    queue = deque()
    
    # Add all 1's to the queue and set their distance to 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j))
                dist[i][j] = 0
    
    # Direction vectors for exploring neighbors
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Perform BFS
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check boundaries and update distance
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    
    return dist

# Example test cases
grid1 = [
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]
print(nearest(grid1))  
# Output: [[1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0]]

grid2 = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 0, 0]
]
print(nearest(grid2))  
# Output: [[0, 1, 0], [0, 0, 1], [0, 1, 2]]
