import heapq

def minimumCostPath(grid):
    # Define directions for movement
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = len(grid)
    
    # Create a cost matrix initialized to infinity
    min_cost = [[float('inf')] * n for _ in range(n)]
    
    # Priority queue for storing (cost, x, y)
    pq = [(grid[0][0], 0, 0)]  # (cost, x, y)
    min_cost[0][0] = grid[0][0]
    
    while pq:
        # Get the current position with the least cost
        current_cost, x, y = heapq.heappop(pq)
        
        # If we reach the bottom-right corner, return the cost
        if x == n - 1 and y == n - 1:
            return current_cost
        
        # Check all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = current_cost + grid[nx][ny]
                
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    
    # Return the cost to reach bottom-right
    return min_cost[n-1][n-1]

# Example test cases
grid1 = [
    [9, 4, 9, 9],
    [6, 7, 6, 4],
    [8, 3, 3, 7],
    [7, 4, 9, 10]
]
print(minimumCostPath(grid1))  # Output: 43

grid2 = [
    [4, 4],
    [3, 7]
]
print(minimumCostPath(grid2))  # Output: 14
