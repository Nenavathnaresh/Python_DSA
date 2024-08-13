from collections import deque

def minThrow(N, arr):
    # Create a board of 30 cells
    board = [-1] * 31
    
    # Fill the board with ladders and snakes
    for i in range(0, 2 * N, 2):
        start = arr[i]
        end = arr[i + 1]
        board[start] = end
    
    # BFS initialization
    queue = deque([(1, 0)])  # (cell, dice throws)
    visited = [False] * 31
    visited[1] = True
    
    while queue:
        current_cell, throws = queue.popleft()
        
        # Check if we've reached the destination cell
        if current_cell == 30:
            return throws
        
        # Try all possible dice rolls from 1 to 6
        for dice in range(1, 7):
            next_cell = current_cell + dice
            if next_cell <= 30 and not visited[next_cell]:
                visited[next_cell] = True
                # If there's a snake or ladder at next_cell, move to that destination
                if board[next_cell] != -1:
                    next_cell = board[next_cell]
                
                queue.append((next_cell, throws + 1))
    
    return -1  # In case there's no valid path, though per problem constraints, there should always be a path.

# Example usage:
N = 8
arr = [3, 22, 5, 8, 11, 26, 20, 29, 17, 4, 19, 7, 27, 1, 21, 9]
print(minThrow(N, arr))  # Output: 3
