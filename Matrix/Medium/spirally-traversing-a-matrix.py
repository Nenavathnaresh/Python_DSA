def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    # Initialize boundaries
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    # Resultant spiral order
    spiral_order = []

    while top <= bottom and left <= right:
        # Traverse from left to right along the top boundary
        for i in range(left, right + 1):
            spiral_order.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom along the right boundary
        for i in range(top, bottom + 1):
            spiral_order.append(matrix[i][right])
        right -= 1

        # Traverse from right to left along the bottom boundary
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral_order.append(matrix[bottom][i])
            bottom -= 1

        # Traverse from bottom to top along the left boundary
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral_order.append(matrix[i][left])
            left += 1

    return spiral_order

# Test cases
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(spiralOrder(matrix1))  # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
print(spiralOrder(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
