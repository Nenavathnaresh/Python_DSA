def findNumberOfGoodComponent(v, e, edges):
    # Build the adjacency list
    adj = {i: [] for i in range(1, v + 1)}
    for u, w in edges:
        adj[u].append(w)
        adj[w].append(u)
    
    visited = [False] * (v + 1)
    
    def dfs(node):
        stack = [node]
        component = []
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                component.append(current)
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return component
    
    good_components_count = 0
    
    for i in range(1, v + 1):
        if not visited[i]:
            component = dfs(i)
            n = len(component)
            # Count edges in this component
            edge_count = 0
            for node in component:
                edge_count += len(adj[node])
            edge_count //= 2  # Each edge is counted twice in the adjacency list
            # Check if it's a fully connected component
            if edge_count == n * (n - 1) // 2:
                good_components_count += 1
    
    return good_components_count

# Example usage:
v = 3
e = 3
edges = [[1, 2], [1, 3], [3, 2]]
print(findNumberOfGoodComponent(v, e, edges))  # Output: 1

v = 7
e = 5
edges = [[1, 2], [7, 2], [3, 5], [3, 4], [4, 5]]
print(findNumberOfGoodComponent(v, e, edges))  # Output: 2
