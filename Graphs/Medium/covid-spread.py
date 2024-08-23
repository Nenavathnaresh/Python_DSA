from collections import deque

def helpaterp(hospital):
    R = len(hospital)
    C = len(hospital[0])
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque()
    uninfected_count = 0
    
    # Initialize the queue with all the infected patients
    for i in range(R):
        for j in range(C):
            if hospital[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif hospital[i][j] == 1:
                uninfected_count += 1
    
    # BFS to infect all the patients
    max_time = 0
    while queue:
        r, c, time = queue.popleft()
        
        # Try to infect adjacent wards
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and hospital[nr][nc] == 1:
                # Infect the uninfected patient
                hospital[nr][nc] = 2
                uninfected_count -= 1
                queue.append((nr, nc, time + 1))
                max_time = time + 1
    
    # Check if all uninfected patients are infected
    if uninfected_count > 0:
        return -1
    else:
        return max_time

# Example usage:
hospital = [
    [2, 1, 0, 2, 1],
    [1, 0, 1, 2, 1],
    [1, 0, 0, 2, 1]
]
print(helpaterp(hospital))  # Output: 2
