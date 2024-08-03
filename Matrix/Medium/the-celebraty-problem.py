def celebrity(M, n):
    # Step 1: Find the candidate
    a = 0
    b = n - 1
    
    while a < b:
        if M[a][b] == 1:
            # a knows b, so a can't be the celebrity
            a += 1
        else:
            # a doesn't know b, so b can't be the celebrity
            b -= 1
    
    # a is now the potential celebrity
    candidate = a
    
    # Step 2: Verify the candidate
    for i in range(n):
        if i != candidate:
            if M[candidate][i] == 1 or M[i][candidate] == 0:
                return -1
    
    return candidate

# Example usage:
M1 = [[0, 1, 0],
      [0, 0, 0], 
      [0, 1, 0]]
print(celebrity(M1, 3))  # Output: 1

M2 = [[0, 1],
      [1, 0]]
print(celebrity(M2, 2))  # Output: -1


########################################## method 2 #########################################

def findCelebrity(mat):
    n = len(mat)
    # Step 1: Find the candidate for celebrity using two-pointer approach
    candidate = 0
    for i in range(1, n):
        if mat[candidate][i] == 1:
            candidate = i
    
    # Step 2: Verify if the candidate is actually a celebrity
    for i in range(n):
        if i != candidate:
            if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                return -1

    return candidate

# Example usage:
mat1 = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
mat2 = [[0, 1], [1, 0]]

print(findCelebrity(mat1))  # Output: 1
print(findCelebrity(mat2))  # Output: -1

