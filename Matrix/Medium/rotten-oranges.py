from collections import deque

def orangesRotting(grid):
    # Directions for up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(grid), len(grid[0])
    
    queue = deque()
    fresh_count = 0

    # Initialize the queue with all the rotten oranges
    # Count the number of fresh oranges
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1
    
    # If no fresh oranges, return 0 immediately
    if fresh_count == 0:
        return 0
    
    # Start BFS
    minutes_passed = 0
    while queue:
        size = len(queue)
        made_progress = False

        for _ in range(size):
            x, y = queue.popleft()

            # Try to rot adjacent fresh oranges
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    # Rot the fresh orange
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    fresh_count -= 1
                    made_progress = True

        # Increment time only if progress was made
        if made_progress:
            minutes_passed += 1

    # Check if there are still fresh oranges left
    return minutes_passed if fresh_count == 0 else -1

# Example usage
grid1 = [
    [0, 1, 2],
    [0, 1, 2],
    [2, 1, 1]
]
print(orangesRotting(grid1))  # Output: 1

grid2 = [
    [2, 2, 0, 1]
]
print(orangesRotting(grid2))  # Output: -1
