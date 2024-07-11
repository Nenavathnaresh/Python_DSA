def largest_connected_1s(grid):
    from collections import defaultdict, deque
    
    n = len(grid)
    if n == 0:
        return 0
    
    def get_neighbors(x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                yield nx, ny

    def bfs(x, y, component_id):
        queue = deque([(x, y)])
        grid[x][y] = component_id
        size = 0
        
        while queue:
            cx, cy = queue.popleft()
            size += 1
            for nx, ny in get_neighbors(cx, cy):
                if grid[nx][ny] == 1:
                    grid[nx][ny] = component_id
                    queue.append((nx, ny))
        
        return size

    component_sizes = {}
    component_id = 2  # Start component IDs from 2 because grid contains 0 and 1.
    
    # Step 1: Identify and label connected components
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                component_sizes[component_id] = bfs(i, j, component_id)
                component_id += 1
    
    max_size = max(component_sizes.values(), default=0)  # Largest original component size
    
    # Step 2: Check changing each 0 to 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                unique_components = set()
                for ni, nj in get_neighbors(i, j):
                    if grid[ni][nj] > 1:
                        unique_components.add(grid[ni][nj])
                
                potential_size = 1 + sum(component_sizes[cid] for cid in unique_components)
                max_size = max(max_size, potential_size)
    
    return max_size

# Example usage
grid1 = [
    [1, 1],
    [0, 1]
]
print(largest_connected_1s(grid1))  # Output: 4

grid2 = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
]
print(largest_connected_1s(grid2))  # Output: 7
