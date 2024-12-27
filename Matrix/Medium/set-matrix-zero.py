def setZeroes(mat):
    n, m = len(mat), len(mat[0])
    first_row_zero, first_col_zero = False, False

    # Step 1: Check if the first row and column contain zero
    for j in range(m):
        if mat[0][j] == 0:
            first_row_zero = True
            break
    for i in range(n):
        if mat[i][0] == 0:
            first_col_zero = True
            break

    # Step 2: Mark rows and columns to be zeroed using the first row and column
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    # Step 3: Set matrix cells to zero based on marks
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0

    # Step 4: Handle the first row and column
    if first_row_zero:
        for j in range(m):
            mat[0][j] = 0
    if first_col_zero:
        for i in range(n):
            mat[i][0] = 0

    return mat

# Example Usage
mat1 = [[1, -1, 1], [-1, 0, 1], [1, -1, 1]]
mat2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

print(setZeroes(mat1))
print(setZeroes(mat2))
