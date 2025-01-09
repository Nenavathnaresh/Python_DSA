def count_pairs_with_sum_less_than_target(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    count = 0

    while left < right:
        if arr[left] + arr[right] < target:
            # Count all pairs between left and right
            count += right - left
            left += 1
        else:
            right -= 1

    return count

# Example Usage
arr1 = [7, 2, 5, 3]
target1 = 8
print(count_pairs_with_sum_less_than_target(arr1, target1))  # Output: 2

arr2 = [5, 2, 3, 2, 4, 1]
target2 = 5
print(count_pairs_with_sum_less_than_target(arr2, target2))  # Output: 4

arr3 = [2, 1, 8, 3, 4, 7, 6, 5]
target3 = 7
print(count_pairs_with_sum_less_than_target(arr3, target3))  # Output: 6
