def sumOfDependencies(V, adj):
    # Sum of dependencies is simply the sum of the lengths of all adjacency lists
    total_dependencies = 0
    
    for i in range(V):
        total_dependencies += len(adj[i])
    
    return total_dependencies

# Example usage:
V = 4
adj = [[2, 3], [3], [3], []]  # Adjacency list representation of the graph
print(sumOfDependencies(V, adj))  # Output: 4

V = 4
adj = [[3, 2, 1], [], [], []]  # Adjacency list representation of the graph
print(sumOfDependencies(V, adj))  # Output: 3
