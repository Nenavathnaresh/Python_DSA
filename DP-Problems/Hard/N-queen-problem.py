def solveNQueens(n):
    def is_safe(board, row, col):
        for c in range(col):
            if board[c] == row or abs(board[c] - row) == abs(c - col):
                return False
        return True

    def solve(col, board, solutions):
        if col == n:
            solutions.append(board[:])
            return
        
        for row in range(1, n + 1):
            if is_safe(board, row, col):
                board[col] = row
                solve(col + 1, board, solutions)
                board[col] = 0  # Backtrack

    solutions = []
    board = [0] * n
    solve(0, board, solutions)
    return solutions

# Example usage:
n1 = 1
print(solveNQueens(n1))  # Output: [[1]]

n4 = 4
print(solveNQueens(n4))  # Output: [[2, 4, 1, 3], [3, 1, 4, 2]]
