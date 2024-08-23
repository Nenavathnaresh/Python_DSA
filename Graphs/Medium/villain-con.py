from collections import deque, defaultdict

def minColour(N, M, mat):
    # Step 1: Build the graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)
    
    for u, v in mat:
        graph[u].append(v)
        in_degree[v] += 1
    
    # Step 2: Topological Sort (Kahn's Algorithm) to find the longest path
    queue = deque()
    distance = [0] * (N + 1)
    
    # Start with all nodes with 0 in-degree
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            distance[i] = 1  # Starting nodes have a distance of 1
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            distance[neighbor] = max(distance[neighbor], distance[node] + 1)
    
    # Step 3: The answer is the maximum value in distance array
    return max(distance)

# Example 1:
N = 5
M = 6
mat = [[1, 3], [2, 3], [3, 4], [1, 4], [2, 5], [3, 5]]
print(minColour(N, M, mat))  # Output: 3

# Example 2:
N = 3
M = 2
mat = [[1, 3], [2, 3]]
print(minColour(N, M, mat))  # Output: 2
