def dfs(node, visited, adj, V):
    visited[node] = True
    
    # Explore all connected vertices
    for j in range(V):
        if adj[node][j] == 1 and not visited[j]:
            dfs(j, visited, adj, V)

def numProvinces(adj, V):
    visited = [False] * V
    provinces = 0
    
    # Iterate through each vertex
    for i in range(V):
        if not visited[i]:
            # Start a DFS for each unvisited vertex
            dfs(i, visited, adj, V)
            provinces += 1  # Count a new province
    
    return provinces

# Example usage:
adj1 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

adj2 = [
    [1, 1],
    [1, 1]
]

print(numProvinces(adj1, 3))  # Output: 2
print(numProvinces(adj2, 2))  # Output: 1
