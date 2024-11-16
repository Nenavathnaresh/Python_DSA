def printTillN(n):
    # Base case: if n is 1, print 1
    if n == 1:
        print(1, end=" ")
        return
    # Recursive call to print numbers from 1 to n-1
    printTillN(n - 1)
    # Print the current number after the recursive call
    print(n, end=" ")

# Example usage:
n = 5
printTillN(n)
print()  # Newline after the output
