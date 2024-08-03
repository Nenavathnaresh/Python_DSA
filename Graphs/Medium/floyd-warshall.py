def shortest_distance(matrix):
    n = len(matrix)
    
    # Initialize the matrix for the Floyd-Warshall algorithm
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = float('inf')  # Treat -1 as infinity

    # Floyd-Warshall algorithm to find the shortest path between every pair
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If both matrix[i][k] and matrix[k][j] are not infinity, update the path
                if matrix[i][k] != float('inf') and matrix[k][j] != float('inf'):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    # Replace all infinities back to -1 to indicate no path exists
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == float('inf'):
                matrix[i][j] = -1

# Example Usage
matrix1 = [[0, 25], [-1, 0]]
shortest_distance(matrix1)
print(matrix1)  # Output: [[0, 25], [-1, 0]]

matrix2 = [[0, 1, 43], [1, 0, 6], [-1, -1, 0]]
shortest_distance(matrix2)
print(matrix2)  # Output: [[0, 1, 7], [1, 0, 6], [-1, -1, 0]]
