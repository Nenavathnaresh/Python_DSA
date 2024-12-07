def isSubSequence(A, B):
    m, n = len(A), len(B)
    i, j = 0, 0  # Pointers for A and B

    # Traverse through B
    while j < n:
        # If characters match, move pointer i
        if i < m and A[i] == B[j]:
            i += 1
        # Move pointer j in all cases
        j += 1

    # Check if all characters of A are found
    return i == m

# Example usage
print(isSubSequence("AXY", "YADXCP"))        # Output: 0 (False)
print(isSubSequence("gksrek", "geeksforgeeks"))  # Output: 1 (True)
