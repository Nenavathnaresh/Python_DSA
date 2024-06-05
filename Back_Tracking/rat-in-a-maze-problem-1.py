def printPath(N, m):
    # Check if the starting or ending point is blocked
    if m[0][0] == 0 or m[N-1][N-1] == 0:
        return []

    def is_safe(x, y):
        return 0 <= x < N and 0 <= y < N and m[x][y] == 1 and not visited[x][y]

    def dfs(x, y, path):
        if x == N-1 and y == N-1:
            paths.append(path)
            return
        
        # Mark this cell as visited
        visited[x][y] = True
        
        # Explore all four directions
        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny):
                dfs(nx, ny, path + move)
        
        # Unmark this cell for other paths (backtracking)
        visited[x][y] = False

    # Directions and their movements (down, up, left, right)
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    paths = []
    visited = [[False] * N for _ in range(N)]
    
    # Start DFS from the starting point
    dfs(0, 0, "")
    
    # Sort paths lexicographically
    paths.sort()
    
    return paths

# Example usage:
N = 4
m = [[1, 0, 0, 0],
     [1, 1, 0, 1], 
     [1, 1, 0, 0],
     [0, 1, 1, 1]]
print(printPath(N, m))  # Output: ['DDRDRR', 'DRDDRR']

N = 2
m = [[1, 0],
     [1, 0]]
print(printPath(N, m))  # Output: []
