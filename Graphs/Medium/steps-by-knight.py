from collections import deque

def minStepToReachTarget(knightPos, targetPos, N):
    # Possible knight moves
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    # Initial and target positions
    start_x, start_y = knightPos
    target_x, target_y = targetPos
    
    # If the starting position is the same as the target
    if (start_x, start_y) == (target_x, target_y):
        return 0
    
    # Initialize the BFS queue and visited set
    queue = deque([(start_x, start_y, 0)])  # (x, y, steps)
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    visited[start_x][start_y] = True
    
    # Perform BFS
    while queue:
        x, y, steps = queue.popleft()
        
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]
            
            if 1 <= new_x <= N and 1 <= new_y <= N and not visited[new_x][new_y]:
                if (new_x, new_y) == (target_x, target_y):
                    return steps + 1
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))
    
    # If we exhaust the queue and never find the target
    return -1
