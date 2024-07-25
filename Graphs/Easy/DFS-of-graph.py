def dfsOfGraph(V, adj):
    # List to store the DFS traversal result
    dfs_traversal = []

    # List to keep track of visited nodes
    visited = [False] * V

    def dfs(node):
        # Mark the node as visited
        visited[node] = True

        # Add the node to the DFS traversal result
        dfs_traversal.append(node)

        # Explore all unvisited neighbors
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    # Start DFS from the 0th node
    dfs(0)

    return dfs_traversal

# Example 1
V1 = 5
adj1 = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(dfsOfGraph(V1, adj1))  # Output: [0, 2, 4, 3, 1]

# Example 2
V2 = 4
adj2 = [[1, 3], [2, 0], [1], [0]]
print(dfsOfGraph(V2, adj2))  # Output: [0, 1, 2, 3]
