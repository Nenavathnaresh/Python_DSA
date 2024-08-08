from collections import deque

def minimumMultiplications(arr, start, end):
    # If start is already equal to end, return 0 steps
    if start == end:
        return 0

    # Initialize BFS queue and visited set
    queue = deque([(start, 0)])  # (current_value, steps)
    visited = set([start])

    # BFS Loop
    while queue:
        current, steps = queue.popleft()

        # Try multiplying with each number in arr
        for num in arr:
            next_value = (current * num) % 100000

            # If we reach the end, return the number of steps
            if next_value == end:
                return steps + 1

            # If this value is not visited, mark and enqueue it
            if next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, steps + 1))

    # If we exhaust the queue without finding the end, return -1
    return -1

# Test cases
arr1 = [2, 5, 7]
start1 = 3
end1 = 30
print(minimumMultiplications(arr1, start1, end1))  # Output: 2

arr2 = [3, 4, 65]
start2 = 7
end2 = 66175
print(minimumMultiplications(arr2, start2, end2))  # Output: 4

arr3 = [10, 20]
start3 = 5
end3 = 1
print(minimumMultiplications(arr3, start3, end3))  # Output: -1
