from collections import deque

# Function to check if the position is inside the board and not visited
def is_inside(x, y, N):
    return 1 <= x <= N and 1 <= y <= N

def minStepToReachTarget(knightPos, targetPos, N):
    # All possible moves of a Knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    
    # Queue for BFS (position_x, position_y, steps)
    queue = deque([(knightPos[0], knightPos[1], 0)])
    
    # Visited array to mark visited positions
    visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    
    # Mark the starting position as visited
    visited[knightPos[0]][knightPos[1]] = True
    
    while queue:
        x, y, steps = queue.popleft()
        
        # If the current position is the target, return the steps count
        if x == targetPos[0] and y == targetPos[1]:
            return steps
        
        # Explore all 8 possible moves of the knight
        for i in range(8):
            new_x, new_y = x + dx[i], y + dy[i]
            
            if is_inside(new_x, new_y, N) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))
    
    # If we exit the loop, it means the target is unreachable
    return -1

# Example usage:
N = 6
knightPos = [4, 5]
targetPos = [1, 1]
print(minStepToReachTarget(knightPos, targetPos, N))  # Output: 3

N = 8
knightPos = [7, 7]
targetPos = [1, 5]
print(minStepToReachTarget(knightPos, targetPos, N))  # Output: 4
