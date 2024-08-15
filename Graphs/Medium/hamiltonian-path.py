def is_hamiltonian_path(adj_list, visited, current, path_count, N):
    # If the path_count equals the number of vertices, we've found a Hamiltonian path
    if path_count == N:
        return True
    
    # Explore all adjacent vertices
    for neighbor in adj_list[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            if is_hamiltonian_path(adj_list, visited, neighbor, path_count + 1, N):
                return True
            visited[neighbor] = False
    
    return False

def check(N, M, Edges):
    # Convert edge list to adjacency list
    adj_list = [[] for _ in range(N + 1)]
    
    for edge in Edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Try starting the path from each vertex
    for start in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[start] = True
        if is_hamiltonian_path(adj_list, visited, start, 1, N):
            return True
    
    return False

# Example usage:
N1 = 4
M1 = 4
Edges1 = [[1, 2], [2, 3], [3, 4], [2, 4]]
print(check(N1, M1, Edges1))  # Output: 1 (True)

N2 = 4
M2 = 3
Edges2 = [[1, 2], [2, 3], [2, 4]]
print(check(N2, M2, Edges2))  # Output: 0 (False)
