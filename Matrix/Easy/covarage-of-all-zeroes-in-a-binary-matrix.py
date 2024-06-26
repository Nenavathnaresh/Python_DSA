def sum_of_coverage(matrix):
    n = len(matrix)
    m = len(matrix[0])
    total_coverage = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # Check left
                if j - 1 >= 0 and matrix[i][j - 1] == 1:
                    total_coverage += 1
                # Check right
                if j + 1 < m and matrix[i][j + 1] == 1:
                    total_coverage += 1
                # Check up
                if i - 1 >= 0 and matrix[i - 1][j] == 1:
                    total_coverage += 1
                # Check down
                if i + 1 < n and matrix[i + 1][j] == 1:
                    total_coverage += 1
    
    return total_coverage

# Example usage:
matrix1 = [[0, 1, 0],
           [0, 1, 1], 
           [0, 0, 0]]
print(sum_of_coverage(matrix1))  # Output: 6

matrix2 = [[0, 1]]
print(sum_of_coverage(matrix2))  # Output: 1
