def frequencyCount(arr, N, P):
    # First step is to decrease all elements by 1 so they are in the range 0 to N-1
    for i in range(N):
        if arr[i] > N:
            arr[i] = 0
    
    # Use elements of the array to record frequency counts
    for i in range(N):
        if arr[i] % (N + 1) > 0:
            arr[(arr[i] % (N + 1)) - 1] += (N + 1)
    
    # Decode the frequency counts
    for i in range(N):
        arr[i] = arr[i] // (N + 1)

# Example usage
arr1 = [2, 3, 2, 3, 5]
N1 = 5
P1 = 5
frequencyCount(arr1, N1, P1)
print(arr1)  # Output: [0, 2, 2, 0, 1]

arr2 = [3, 3, 3, 3]
N2 = 4
P2 = 3
frequencyCount(arr2, N2, P2)
print(arr2)  # Output: [0, 0, 4, 0]

arr3 = [8, 9]
N3 = 2
P3 = 9
frequencyCount(arr3, N3, P3)
print(arr3)  # Output: [0, 0]
