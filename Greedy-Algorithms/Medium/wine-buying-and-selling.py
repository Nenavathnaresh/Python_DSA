def wineSelling(arr, n):
    total_work = 0
    current_balance = 0

    for i in range(n):
        current_balance += arr[i]
        total_work += abs(current_balance)

    return total_work

# Example usage:
N1 = 5
Arr1 = [5, -4, 1, -3, 1]
print(wineSelling(Arr1, N1))  # Output: 9

N2 = 6
Arr2 = [-1000, -1000, -1000, 1000, 1000, 1000]
print(wineSelling(Arr2, N2))  # Output: 9000
