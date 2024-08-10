def findMotherVertex(V, adj):
    def dfs(v, visited):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited)
    
    visited = [False] * V
    last_finished_vertex = -1
    
    # Perform DFS on each vertex to find the last finished vertex
    for i in range(V):
        if not visited[i]:
            dfs(i, visited)
            last_finished_vertex = i
    
    # Reset visited array and verify the last finished vertex
    visited = [False] * V
    dfs(last_finished_vertex, visited)
    
    # If all vertices are visited, then last_finished_vertex is a Mother Vertex
    if all(visited):
        return last_finished_vertex
    else:
        return -1

# Example Test Cases
V1 = 4
adj1 = [[1, 2], [3], [], []]
print(findMotherVertex(V1, adj1))  # Output: 0

V2 = 3
adj2 = [[1, 2], [2], []]
print(findMotherVertex(V2, adj2))  # Output: 0

V3 = 3
adj3 = [[1], [2], [0]]
print(findMotherVertex(V3, adj3))  # Output: 2
