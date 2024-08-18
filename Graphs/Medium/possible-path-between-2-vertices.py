def countPaths(V, adj, source, destination):
    # Initialize the path count
    path_count = [0]  # Using a list to allow modification within the dfs function

    # Helper function to perform DFS
    def dfs(node):
        # If we reach the destination, increment the path count
        if node == destination:
            path_count[0] += 1
            return
        
        # Explore all neighbors
        for neighbor in adj[node]:
            dfs(neighbor)
    
    # Start DFS from the source node
    dfs(source)
    
    # Return the total number of paths found
    return path_count[0]

# Example usage:
V = 5
E = 7
adj = [{1, 2, 4}, {3, 4}, {4}, {2}, {}]
source = 0
destination = 4
print(countPaths(V, adj, source, destination))  # Output: 4

V = 4
E = 5
adj = [{1, 3}, {2, 3}, {3}, {}]
source = 0
destination = 3
print(countPaths(V, adj, source, destination))  # Output: 3
