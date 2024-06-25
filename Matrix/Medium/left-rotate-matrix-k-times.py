class Solution:
    def rotate_matrix_left(self, k, mat):
        rows = len(mat)
        cols = len(mat[0])
        # Effective rotations needed
        k = k % cols
        # Create a new matrix for the result
        result = [[0] * cols for _ in range(rows)]
        
        # Rotate each row
        for i in range(rows):
            for j in range(cols):
                new_col = (j - k) % cols
                result[i][new_col] = mat[i][j]
        
        return result

# Example usage:
if __name__ == "__main__":
    k1 = 1
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    k2 = 2
    mat2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Create an instance of the Solution class
    ob = Solution()

    # Rotate the matrices
    result1 = ob.rotate_matrix_left(k1, mat1)
    result2 = ob.rotate_matrix_left(k2, mat2)

    # Print results
    for row in result1:
        print(' '.join(map(str, row)))

    print()  # For better readability between test cases

    for row in result2:
        print(' '.join(map(str, row)))
