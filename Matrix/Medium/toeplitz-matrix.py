def isToeplitz(mat):
    rows = len(mat)
    cols = len(mat[0])
    
    for r in range(1, rows):
        for c in range(1, cols):
            if mat[r][c] != mat[r - 1][c - 1]:
                return 0
    return 1

# Test cases
mat1 = [[6, 7, 8],
        [4, 6, 7],
        [1, 4, 6]]
print(isToeplitz(mat1))  # Output: 1

mat2 = [[1, 2, 3],
        [4, 5, 6]]
print(isToeplitz(mat2))  # Output: 0
