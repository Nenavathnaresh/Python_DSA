from collections import deque

def findDistance(M, N, A):
    # Initialize the result matrix with the same dimensions as A
    result = [[float('inf')] * N for _ in range(M)]
    queue = deque()
    
    # Initialize the BFS with all bomb positions
    for i in range(M):
        for j in range(N):
            if A[i][j] == 'B':
                result[i][j] = 0
                queue.append((i, j))
            elif A[i][j] == 'W':
                result[i][j] = -1
    
    # Directions array for exploring 4 neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS to calculate the shortest distance
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < M and 0 <= ny < N and A[nx][ny] == 'O':
                if result[nx][ny] > result[x][y] + 1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))
    
    # Replace infinity with -1 where there is no valid path to a bomb
    for i in range(M):
        for j in range(N):
            if result[i][j] == float('inf'):
                result[i][j] = -1
    
    return result

# Example usage:
N = 3
M = 3
A = [
  ['O', 'O', 'O'], 
  ['W', 'B', 'B'], 
  ['W', 'O', 'O']
]
output = findDistance(N, M, A)
for row in output:
    print(row)
