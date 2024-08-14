def dfs(v, visited, adj, c, d):
    visited[v] = True
    for neighbor in adj[v]:
        if (v == c and neighbor == d) or (v == d and neighbor == c):
            continue  # Skip the edge c-d
        if not visited[neighbor]:
            dfs(neighbor, visited, adj, c, d)

def isBridge(V, adj, c, d):
    # Initialize visited array
    visited = [False] * V
    
    # Perform DFS starting from vertex c
    dfs(c, visited, adj, c, d)
    
    # If d is not visited, then c-d is a bridge
    if not visited[d]:
        return 1
    else:
        return 0

# Example usage:
V = 5
adj = [[1, 2], [0, 2], [0, 1, 3], [2, 4], [3]]
c, d = 1, 2
print(isBridge(V, adj, c, d))  # Output: 0

V = 4
adj = [[1], [0, 2], [1, 3], [2]]
c, d = 1, 2
print(isBridge(V, adj, c, d))  # Output: 1
