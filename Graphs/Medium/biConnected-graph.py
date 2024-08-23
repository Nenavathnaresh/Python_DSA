def is_biconnected(n, e, arr):
    if n == 1:
        return True  # A single vertex is trivially biconnected.
    
    # Create the adjacency list
    adj = [[] for _ in range(n)]
    for i in range(0, len(arr), 2):
        u = arr[i]
        v = arr[i + 1]
        adj[u].append(v)
        adj[v].append(u)
    
    # Variables to store discovery time and low values
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    time = 0
    
    # To store the articulation points
    def dfs(u):
        nonlocal time
        disc[u] = low[u] = time
        time += 1
        children = 0  # Count of children in DFS tree

        for v in adj[u]:
            if disc[v] == -1:  # If v is not visited
                parent[v] = u
                children += 1
                if not dfs(v):
                    return False
                
                # Check if the subtree rooted at v has a connection back to one of the ancestors of u
                low[u] = min(low[u], low[v])

                # (1) If u is the root of DFS tree and has two or more children, it's an articulation point
                if parent[u] == -1 and children > 1:
                    return False

                # (2) If u is not root and low value of one of its children is more than discovery value of u
                if parent[u] != -1 and low[v] >= disc[u]:
                    return False
            elif v != parent[u]:  # Update low value of u for parent function calls
                low[u] = min(low[u], disc[v])
        return True
    
    # Start DFS from the first vertex
    if not dfs(0):
        return 0

    # Check if all vertices are visited
    for i in range(n):
        if disc[i] == -1:
            return 0  # If any vertex is not visited, the graph is not connected

    return 1

# Example 1:
n = 2
e = 1
arr = [0, 1]
print(is_biconnected(n, e, arr))  # Output: 1

# Example 2:
n = 3
e = 2
arr = [0, 1, 1, 2]
print(is_biconnected(n, e, arr))  # Output: 0
