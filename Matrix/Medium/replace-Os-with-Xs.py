def fill(N, M, mat):
    def dfs(r, c):
        if r < 0 or r >= N or c < 0 or c >= M or mat[r][c] != 'O':
            return
        # Mark this 'O' as temporarily protected
        mat[r][c] = 'T'
        # Perform DFS in all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    # Step 1: Mark all boundary-connected 'O's with 'T'
    for i in range(N):
        if mat[i][0] == 'O':
            dfs(i, 0)
        if mat[i][M - 1] == 'O':
            dfs(i, M - 1)
    for j in range(M):
        if mat[0][j] == 'O':
            dfs(0, j)
        if mat[N - 1][j] == 'O':
            dfs(N - 1, j)
    
    # Step 2: Transform the matrix
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 'O':
                mat[i][j] = 'X'
            elif mat[i][j] == 'T':
                mat[i][j] = 'O'
    
    return mat

# Example usage:
n = 5
m = 4
mat = [['X', 'X', 'X', 'X'], 
       ['X', 'O', 'X', 'X'], 
       ['X', 'O', 'O', 'X'], 
       ['X', 'O', 'X', 'X'], 
       ['X', 'X', 'O', 'O']]
result = fill(n, m, mat)
for row in result:
    print(row)
