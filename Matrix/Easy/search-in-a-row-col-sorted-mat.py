def searchMatrix(mat, x):
    n = len(mat)       # Number of rows
    m = len(mat[0])    # Number of columns

    # Start from the top-right corner
    row, col = 0, m - 1

    while row < n and col >= 0:
        if mat[row][col] == x:
            return True  # Found x
        elif mat[row][col] > x:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False  # x not found

# Example Usage
mat1 = [[3, 30, 38], [20, 52, 54], [35, 60, 69]]
x1 = 62
print(searchMatrix(mat1, x1))  # Output: False

mat2 = [[18, 21, 27], [38, 55, 67]]
x2 = 55
print(searchMatrix(mat2, x2))  # Output: True

mat3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x3 = 3
print(searchMatrix(mat3, x3))  # Output: True
