def isNegativeWeightCycle(n, edges):
    # Initialize distances from source to all other vertices as INFINITE
    dist = [float('inf')] * n
    
    # Loop over each node to ensure that even disconnected components are checked
    for start_node in range(n):
        dist[start_node] = 0  # Start from this node
        
        # Relax all edges |V| - 1 times.
        for i in range(n - 1):
            for u, v, weight in edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        
        # Check for negative-weight cycles.
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                return 1  # Negative weight cycle found
        
        # Reset distances for the next starting node
        dist = [float('inf')] * n
    
    return 0  # No negative weight cycle found

# Example Usage:
n = 5
edges = [[1, 0, 5], [1, 2, -2], [1, 4, 6], [2, 3, 3], [3, 1, -4]]
print(isNegativeWeightCycle(n, edges))  # Output: 1
