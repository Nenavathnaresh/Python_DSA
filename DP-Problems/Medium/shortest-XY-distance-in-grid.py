from collections import deque

# Direction vectors for moving in 4 directions (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def shortestXYDist(N, M, grid):
    # Queue for BFS
    queue = deque()
    
    # Visited array to keep track of visited cells
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    # First, enqueue all the 'X' cells
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'X':
                queue.append((i, j, 0))  # (row, col, distance)
                visited[i][j] = True
    
    # Perform BFS
    while queue:
        row, col, dist = queue.popleft()
        
        # Check if we have reached a 'Y' cell
        if grid[row][col] == 'Y':
            return dist
        
        # Explore the 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check if the new position is within bounds and not visited
            if 0 <= new_row < N and 0 <= new_col < M and not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, dist + 1))
    
    # Should not reach here as there's guaranteed to be at least one 'X' and one 'Y'
    return -1

# Example usage:
grid1 = [
    ['X', 'O', 'O', 'O'],
    ['O', 'Y', 'O', 'Y'],
    ['X', 'X', 'O', 'O'],
    ['O', 'Y', 'O', 'O']
]
N1, M1 = 4, 4
print(shortestXYDist(N1, M1, grid1))  # Output: 1

grid2 = [
    ['X', 'X', 'O'],
    ['O', 'O', 'Y'],
    ['Y', 'O', 'O']
]
N2, M2 = 3, 3
print(shortestXYDist(N2, M2, grid2))  # Output: 2


#########################################################################################\

import sys

def shortestXYDist(N, M, grid):
    # Initialize the DP table with a large value for all cells
    INF = sys.maxsize
    dist = [[INF for _ in range(M)] for _ in range(N)]
    
    # First pass: top-left to bottom-right
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'X':
                dist[i][j] = 0  # Distance from 'X' to itself is 0
            else:
                # Check top and left neighbors
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)

    # Second pass: bottom-right to top-left
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if grid[i][j] != 'X':
                # Check bottom and right neighbors
                if i < N-1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < M-1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)

    # Now find the minimum distance for all 'Y' cells
    min_distance = INF
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'Y':
                min_distance = min(min_distance, dist[i][j])

    return min_distance

# Example usage:
grid1 = [
    ['X', 'O', 'O', 'O'],
    ['O', 'Y', 'O', 'Y'],
    ['X', 'X', 'O', 'O'],
    ['O', 'Y', 'O', 'O']
]
N1, M1 = 4, 4
print(shortestXYDist(N1, M1, grid1))  # Output: 1

grid2 = [
    ['X', 'X', 'O'],
    ['O', 'O', 'Y'],
    ['Y', 'O', 'O']
]
N2, M2 = 3, 3
print(shortestXYDist(N2, M2, grid2))  # Output: 2
