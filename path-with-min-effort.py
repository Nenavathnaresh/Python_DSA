import heapq

def MinimumEffort(rows, columns, heights):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    min_effort = [[float('inf')] * columns for _ in range(rows)]
    min_effort[0][0] = 0
    pq = [(0, 0, 0)]  # (effort, row, col)

    while pq:
        effort, row, col = heapq.heappop(pq)
        if row == rows - 1 and col == columns - 1:
            return effort

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < columns:
                new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                if new_effort < min_effort[new_row][new_col]:
                    min_effort[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))

# Test cases
print(MinimumEffort(3, 3, [[1,2,2],[3,8,2],[5,3,5]]))  # Output: 2
print(MinimumEffort(2, 2, [[7,7],[7,7]]))  # Output: 0
