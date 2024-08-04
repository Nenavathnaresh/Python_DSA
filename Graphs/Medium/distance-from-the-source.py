def bellman_ford(V, edges, S):
    # Initialize distances with a large number
    inf = 100000000  # 10^8
    dist = [inf] * V
    dist[S] = 0
    
    # Relax edges V-1 times
    for i in range(V - 1):
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != inf and dist[u] + w < dist[v]:
            return [-1]  # Negative cycle detected

    # Replace inf distances with 10^8
    for i in range(V):
        if dist[i] == inf:
            dist[i] = 100000000

    return dist

# Example 1
E1 = [[0, 1, 9]]
S1 = 0
print(bellman_ford(2, E1, S1))  # Expected Output: [0, 9]

# Example 2
E2 = [[0, 1, 5], [1, 0, 3], [1, 2, -1], [2, 0, 1]]
S2 = 2
print(bellman_ford(3, E2, S2))  # Expected Output: [1, 6, 0]
