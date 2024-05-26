def trappingWater(arr, n):
    if n <= 2:
        return 0  # No water can be trapped if there are less than 3 blocks

    # Arrays to store the maximum height to the left and right of each block
    left_max = [0] * n
    right_max = [0] * n

    # Fill the left_max array
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], arr[i])

    # Fill the right_max array
    right_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], arr[i])

    # Calculate the total water trapped
    water_trapped = 0
    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - arr[i]

    return water_trapped

# Example usage:
N1 = 6
arr1 = [3,0,0,2,0,4]
print(trappingWater(arr1, N1))  # Output: 10

N2 = 4
arr2 = [7,4,0,9]
print(trappingWater(arr2, N2))  # Output: 10

N3 = 3
arr3 = [6,9,9]
print(trappingWater(arr3, N3))  # Output: 0
