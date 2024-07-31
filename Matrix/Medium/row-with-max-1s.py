def row_with_max_ones(arr):
    n = len(arr)
    m = len(arr[0])
    max_row_index = -1
    max_ones = -1
    current_column = m - 1

    for i in range(n):
        while current_column >= 0 and arr[i][current_column] == 1:
            current_column -= 1
        # Number of 1's in the current row is from current_column + 1 to m - 1
        number_of_ones = m - (current_column + 1)
        
        if number_of_ones > max_ones:
            max_ones = number_of_ones
            max_row_index = i

    return max_row_index

# Test cases
arr1 = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

arr2 = [
    [0, 0],
    [1, 1]
]

print(row_with_max_ones(arr1))  # Output: 2
print(row_with_max_ones(arr2))  # Output: 1

######################################################################################################


# def rowWithMax1s(arr):
# 	max_count = 0
# 	ind = -1
# 	for i in range(len(arr)):
# 		count = 0
# 		for j in range(len(arr[0])):
# 		    if(arr[i][j] == 1):
# 		        count += 1 
# 		if max_count < count:
# 		    max_count = count 
# 		    ind = i
# 	return ind