def isEulerCircuitExist(v, adj):
    # Function to perform DFS
    def dfs(node, visited):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited)
    
    # Step 1: Check if all vertices with a non-zero degree have even degree
    for i in range(v):
        if len(adj[i]) % 2 != 0:
            return 0  # If any vertex has an odd degree, return 0
    
    # Step 2: Check connectivity of all vertices with non-zero degree
    visited = [False] * v
    start_node = -1
    
    # Find a vertex with a non-zero degree
    for i in range(v):
        if len(adj[i]) > 0:
            start_node = i
            break
    
    if start_node == -1:
        return 1  # All vertices have 0 degree, the graph trivially has an Eulerian circuit
    
    # Perform DFS starting from a vertex with a non-zero degree
    dfs(start_node, visited)
    
    # Check if all vertices with a non-zero degree were visited
    for i in range(v):
        if len(adj[i]) > 0 and not visited[i]:
            return 0
    
    return 1  # All conditions satisfied, Eulerian circuit exists

# Example usage:
v = 4
edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
adj = [[] for _ in range(v)]
for u, w in edges:
    adj[u].append(w)
    adj[w].append(u)
print(isEulerCircuitExist(v, adj))  # Output: 1

v = 3
edges = [[0, 1], [0, 2]]
adj = [[] for _ in range(v)]
for u, w in edges:
    adj[u].append(w)
    adj[w].append(u)
print(isEulerCircuitExist(v, adj))  # Output: 0
