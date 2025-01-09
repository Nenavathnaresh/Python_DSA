def closestPair(arr, target):
    if len(arr) < 2:
        return []

    # Sort the array
    arr.sort()

    # Initialize variables
    left, right = 0, len(arr) - 1
    closest_sum = float('inf')
    result_pair = []

    while left < right:
        current_sum = arr[left] + arr[right]
        abs_diff = abs(arr[right] - arr[left])

        # Update the result if conditions are met
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
            result_pair = [arr[left], arr[right]]
        elif abs(current_sum - target) == abs(closest_sum - target):
            if abs_diff > abs(result_pair[1] - result_pair[0]):
                result_pair = [arr[left], arr[right]]

        # Move pointers
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return result_pair
