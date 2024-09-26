def max_consecutive_steps(arr):
    max_steps = 0
    current_steps = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_steps += 1
            max_steps = max(max_steps, current_steps)
        else:
            current_steps = 0  # Reset the current step count

    return max_steps

# Example test cases
arr1 = [1, 2, 2, 3, 2]
arr2 = [1, 2, 3, 4]

print(max_consecutive_steps(arr1))  # Output: 1
print(max_consecutive_steps(arr2))  # Output: 3
