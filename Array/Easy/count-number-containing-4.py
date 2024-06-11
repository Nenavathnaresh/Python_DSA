def count_numbers_with_four(n):
    count = 0

    for i in range(1, n + 1):
        if '4' in str(i):
            count += 1

    return count

# Test cases
print(count_numbers_with_four(9))    # Expected output: 1
print(count_numbers_with_four(14))   # Expected output: 2
print(count_numbers_with_four(40))   # Expected output: 9
print(count_numbers_with_four(50))   # Expected output: 14
print(count_numbers_with_four(100))  # Expected output: 19
