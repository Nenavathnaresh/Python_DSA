def jugglerSequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n ** (1 / 2))
        else:
            n = int(n ** (3 / 2))
        sequence.append(n)
    return sequence

# Test cases
print(jugglerSequence(9))  # Output: [9, 27, 140, 11, 36, 6, 2, 1]
print(jugglerSequence(6))  # Output: [6, 2, 1]
