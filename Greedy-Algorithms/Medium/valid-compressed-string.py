def checkCompressed(S, T):
    i, j = 0, 0
    n, m = len(S), len(T)
    
    while j < m:
        if T[j].isdigit():
            # Extract the full number
            num = 0
            while j < m and T[j].isdigit():
                num = num * 10 + int(T[j])
                j += 1
            i += num
        else:
            if i < n and S[i] == T[j]:
                i += 1
                j += 1
            else:
                return 0
    
    # Check if both pointers reached the end of their respective strings
    return 1 if i == n else 0

# Example usage:
print(checkCompressed("GEEKSFORGEEKS", "G7G3S"))  # Output: 1
print(checkCompressed("DFS", "D1D"))              # Output: 0
