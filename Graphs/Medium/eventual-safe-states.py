from collections import deque, defaultdict

def eventualSafeNodes(V, adj):
    # Reverse the graph
    rev_adj = defaultdict(list)
    in_degree = [0] * V

    for u in range(V):
        for v in adj[u]:
            rev_adj[v].append(u)
            in_degree[u] += 1

    # Queue to store nodes with zero in-degree
    queue = deque()
    
    # Nodes with no outgoing edges are safe
    for i in range(V):
        if in_degree[i] == 0:
            queue.append(i)
    
    safe_nodes = []
    
    while queue:
        node = queue.popleft()
        safe_nodes.append(node)
        
        for neighbor in rev_adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    safe_nodes.sort()
    return safe_nodes

# Example usage:
V = 7
adj = [
    [1, 2], # edges from node 0
    [2, 3], # edges from node 1
    [5],    # edges from node 2
    [0],    # edges from node 3
    [5],    # edges from node 4
    [],     # edges from node 5 (terminal node)
    []      # edges from node 6 (terminal node)
]

print(eventualSafeNodes(V, adj))  # Output: [2, 4, 5, 6]
