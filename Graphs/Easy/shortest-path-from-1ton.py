def minimumStep(n):
    steps = 0
    while n > 1:
        if n % 3 == 0:
            n //= 3  # If divisible by 3, divide
        else:
            n -= 1   # Else, subtract 1
        steps += 1
    return steps

# Example Test Cases
print(minimumStep(9))  # Output: 2
print(minimumStep(4))  # Output: 2


#########################################################################################

from collections import deque

def minimumStep(n):
    if n == 1:
        return 0  # Already at the target

    # BFS queue: holds tuples of (current_vertex, number_of_edges)
    queue = deque([(1, 0)])  # Start at vertex 1 with 0 edges

    # Visited array to keep track of explored vertices
    visited = [False] * (n + 1)
    visited[1] = True

    # BFS loop
    while queue:
        current_vertex, edges = queue.popleft()

        # Calculate possible next moves
        next_vertices = [current_vertex + 1, current_vertex * 3]

        for next_vertex in next_vertices:
            if next_vertex == n:
                return edges + 1  # Found the target
            if next_vertex <= n and not visited[next_vertex]:
                visited[next_vertex] = True
                queue.append((next_vertex, edges + 1))
    
    return -1  # If n cannot be reached, though problem guarantees reachability

# Example Test Cases
print(minimumStep(9))  # Output: 2
print(minimumStep(4))  # Output: 2
