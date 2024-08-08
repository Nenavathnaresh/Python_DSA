def kosaraju(V, adj):
    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)
    
    def reverse_graph(V, adj):
        rev_adj = [[] for _ in range(V)]
        for v in range(V):
            for neighbor in adj[v]:
                rev_adj[neighbor].append(v)
        return rev_adj
    
    def dfs_transpose(v, visited, rev_adj):
        visited[v] = True
        for neighbor in rev_adj[v]:
            if not visited[neighbor]:
                dfs_transpose(neighbor, visited, rev_adj)
    
    # Step 1: Perform DFS on the original graph and store the finish order in a stack
    stack = []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            dfs(i, visited, stack)
    
    # Step 2: Create the transpose of the graph
    rev_adj = reverse_graph(V, adj)
    
    # Step 3: Perform DFS on the transpose graph in the order defined by the stack
    visited = [False] * V
    scc_count = 0
    while stack:
        v = stack.pop()
        if not visited[v]:
            # Perform DFS from vertex v in the transposed graph
            dfs_transpose(v, visited, rev_adj)
            scc_count += 1  # Each DFS call on the transposed graph finds one SCC
    
    return scc_count

# Test cases
V1 = 5
adj1 = [
    [1],
    [2],
    [0, 3],
    [4],
    []
]
print(kosaraju(V1, adj1))  # Output: 3

V2 = 4
adj2 = [
    [1, 2],
    [2, 3],
    [3],
    []
]
print(kosaraju(V2, adj2))  # Output: 4
