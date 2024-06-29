def is_palindrome(arr):
    return arr == arr[::-1]

def find_palindrome(arr):
    n = len(arr)
    
    # Check each row
    for i in range(n):
        if is_palindrome(arr[i]):
            return f"{i} R"
    
    # Check each column
    for j in range(n):
        column = [arr[i][j] for i in range(n)]
        if is_palindrome(column):
            return f"{j} C"
    
    return "-1"

# Test cases
arr1 = [[1, 0, 0], 
        [0, 1, 0],
        [1, 1, 0]]
print(find_palindrome(arr1))  # Output: "1 R"

arr2 = [[1, 0],
        [1, 0]]
print(find_palindrome(arr2))  # Output: "0 C"
