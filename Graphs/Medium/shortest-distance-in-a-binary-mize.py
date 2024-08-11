from collections import deque

def shortestPath(grid, source, destination):
    n, m = len(grid), len(grid[0])
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS queue: (row, col, distance from source)
    queue = deque([(source[0], source[1], 0)])
    
    # Mark the source cell as visited
    grid[source[0]][source[1]] = 0
    
    while queue:
        r, c, dist = queue.popleft()
        
        # If we reached the destination
        if (r, c) == (destination[0], destination[1]):
            return dist
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                queue.append((nr, nc, dist + 1))
                # Mark as visited
                grid[nr][nc] = 0
    
    # If we exit the loop, no path was found
    return -1

# Example usage:
grid1 = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 1]
]
source1 = (0, 1)
destination1 = (2, 2)
print(shortestPath(grid1, source1, destination1))  # Output: 3

grid2 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 0, 1, 0, 1]
]
source2 = (0, 0)
destination2 = (3, 4)
print(shortestPath(grid2, source2, destination2))  # Output: -1
