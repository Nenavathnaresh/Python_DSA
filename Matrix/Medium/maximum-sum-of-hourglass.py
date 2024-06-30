def findMaxSum(n,m,mat):
    max_sum = -1 
    
    if m<3 or n<3:
        return -1 
    
    for i in range(n-2):
        for j in range(m-2):
            sum = (mat[i][j] + mat[i][j+1]+mat[i][j+2])+(mat[i+1][j+1])+(mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2])
            max_sum = max(max_sum, sum)
    return max_sum


n, m = 3, 3
mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(findMaxSum(n, m, mat1))  # Output: 35