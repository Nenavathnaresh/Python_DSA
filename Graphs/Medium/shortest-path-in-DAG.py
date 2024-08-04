from collections import defaultdict, deque

def topological_sort_dag(V, adj_list):
    in_degree = [0] * V
    # Calculate in-degree for each vertex
    for u in range(V):
        for v, _ in adj_list[u]:
            in_degree[v] += 1
    
    # Queue for vertices with zero in-degree
    queue = deque()
    for i in range(V):
        if in_degree[i] == 0:
            queue.append(i)
    
    top_order = []
    while queue:
        u = queue.popleft()
        top_order.append(u)
        for v, _ in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return top_order

def shortest_path(N, M, edges):
    # Initialize adjacency list
    adj_list = defaultdict(list)
    for u, v, weight in edges:
        adj_list[u].append((v, weight))
    
    # Topological sort
    topo_order = topological_sort_dag(N, adj_list)
    
    # Initialize distances
    inf = float('inf')
    distances = [inf] * N
    distances[0] = 0  # Distance to source is 0
    
    # Process vertices in topological order
    for u in topo_order:
        if distances[u] != inf:
            for v, weight in adj_list[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Replace inf with -1 for unreachable vertices
    distances = [-1 if dist == inf else dist for dist in distances]
    
    return distances

# Example 1
N1 = 4
M1 = 2  
edges1 = [[0, 1, 2], [0, 2, 1]]
print(shortest_path(N1, M1, edges1))  # Expected Output: [0, 2, 1, -1]

# Example 2
N2 = 6
M2 = 7
edges2 = [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]
print(shortest_path(N2, M2, edges2))  # Expected Output: [0, 2, 3, 6, 1, 5]
