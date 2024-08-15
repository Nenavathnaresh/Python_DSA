def isConnected(V, adj, visited, start):
    # A utility function to do DFS
    stack = [start]
    visited[start] = True
    
    while stack:
        node = stack.pop()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

def isEulerCircuit(V, adj):
    # Check if all vertices with non-zero degree are connected
    visited = [False] * V
    
    # Find a vertex with a non-zero degree
    start = -1
    for i in range(V):
        if len(adj[i]) > 0:
            start = i
            break
    
    # If there are no edges in the graph
    if start == -1:
        return 2
    
    # Start DFS from a vertex with non-zero degree
    isConnected(V, adj, visited, start)
    
    # Check if all vertices with non-zero degree are visited
    for i in range(V):
        if not visited[i] and len(adj[i]) > 0:
            return 0
    
    # Count vertices with odd degree
    odd_count = 0
    for i in range(V):
        if len(adj[i]) % 2 != 0:
            odd_count += 1
    
    # If odd_count is 0, then it's an Eulerian Circuit
    if odd_count == 0:
        return 2
    # If odd_count is 2, then it's an Eulerian Path
    elif odd_count == 2:
        return 1
    # Otherwise, it's neither
    else:
        return 0

# Example usage
V1 = 3
adj1 = [[1, 2], [0, 2], [0, 1]]
print(isEulerCircuit(V1, adj1))  # Output: 2 (Eulerian Circuit)

V2 = 3
adj2 = [[1], [0, 2], [1]]
print(isEulerCircuit(V2, adj2))  # Output: 1 (Eulerian Path)

V3 = 4
adj3 = [[1], [0, 2], [1, 3], [2]]
print(isEulerCircuit(V3, adj3))  # Output: 0 (Neither)
