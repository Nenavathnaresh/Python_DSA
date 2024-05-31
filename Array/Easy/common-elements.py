def commonElements(A, B, C, n1, n2, n3):
    i, j, k = 0, 0, 0
    result = []

    while i < n1 and j < n2 and k < n3:
        # If A[i], B[j], and C[k] are equal, add to the result and move all pointers
        if A[i] == B[j] == C[k]:
            if len(result) == 0 or result[-1] != A[i]:
                result.append(A[i])
            i += 1
            j += 1
            k += 1
        # Move pointer for the smallest value
        elif A[i] < B[j]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else:
            k += 1
    
    return result if result else [-1]

# Example usage
n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]

print(commonElements(A, B, C, n1, n2, n3))  # Output: [20, 80]
