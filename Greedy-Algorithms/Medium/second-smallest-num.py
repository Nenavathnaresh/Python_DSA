def secondSmallest(S, D):
    # Special case when D is 1
    if D == 1:
        if 0 <= S <= 9:
            return str(S)
        else:
            return "-1"

    # Step 1: Form the smallest number with sum S and D digits
    if S == 0 or S > 9 * D:
        return "-1"  # Not possible to form such a number

    # Initialize the result array
    result = [0] * D

    # Ensure the first digit is non-zero
    result[0] = 1
    S -= 1

    # Fill the rest of the digits from the least significant position
    for i in range(D - 1, -1, -1):
        if S > 9:
            result[i] += 9
            S -= 9
        else:
            result[i] += S
            S = 0

    # Convert result array to the smallest number
    smallest_number = ''.join(map(str, result))

    # Step 2: Form the second smallest number by slightly modifying the smallest one
    for i in range(D - 2, -1, -1):
        if result[i] < 9 and result[i + 1] > 0:
            result[i] += 1
            result[i + 1] -= 1
            break
    else:
        return "-1"

    # Convert result array to the second smallest number
    second_smallest_number = ''.join(map(str, result))

    return second_smallest_number

# Example usage:
print(secondSmallest(9, 2))  # Output: 27
print(secondSmallest(16, 3)) # Output: 178
print(secondSmallest(26, 3)) # Output: 989
print(secondSmallest(6, 1))  # Output: 6
