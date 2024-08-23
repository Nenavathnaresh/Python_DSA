def Solve(n, edges):
    parent = list(range(n))
    rank = [1] * n
    redundant_edges = 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
        else:
            return False
        return True

    for u, v in edges:
        if not union(u, v):
            redundant_edges += 1

    components = len(set(find(x) for x in range(n)))
    
    # We need at least (components - 1) edges to connect the graph
    if redundant_edges >= components - 1:
        return components - 1
    else:
        return -1

# Example usage:
n1 = 4
edges1 = [[0, 1], [0, 2], [1, 2]]
print(Solve(n1, edges1))  # Output: 1

n2 = 6
edges2 = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
print(Solve(n2, edges2))  # Output: 2
