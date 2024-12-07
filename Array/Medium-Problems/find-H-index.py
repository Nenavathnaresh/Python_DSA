def hIndex(citations):
    n = len(citations)
    bucket = [0] * (n + 1)

    # Step 1: Fill the buckets
    for c in citations:
        if c >= n:
            bucket[n] += 1
        else:
            bucket[c] += 1

    # Step 2: Calculate the H-Index
    running_sum = 0
    for i in range(n, -1, -1):
        running_sum += bucket[i]
        if running_sum >= i:
            return i

    return 0

# Example Test Cases
print(hIndex([3, 0, 5, 3, 0]))  # Output: 3
print(hIndex([5, 1, 2, 4, 1]))  # Output: 2
print(hIndex([0, 0]))           # Output: 0
