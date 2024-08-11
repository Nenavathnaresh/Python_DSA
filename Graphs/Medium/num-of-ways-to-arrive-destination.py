import heapq

def countPaths(n, roads):
    MOD = 10**9 + 7
    adj = [[] for _ in range(n)]
    
    for u, v, t in roads:
        adj[u].append((v, t))
        adj[v].append((u, t))
    
    # Distance array initialized to infinity
    dist = [float('inf')] * n
    # Ways array to count the number of shortest paths
    count = [0] * n
    
    # Min-heap for Dijkstra's algorithm
    pq = [(0, 0)]  # (distance, node)
    dist[0] = 0
    count[0] = 1
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        for v, time in adj[u]:
            if dist[u] + time < dist[v]:
                dist[v] = dist[u] + time
                heapq.heappush(pq, (dist[v], v))
                count[v] = count[u]  # new shortest path
            elif dist[u] + time == dist[v]:
                count[v] = (count[v] + count[u]) % MOD  # additional shortest path
    
    return count[n-1] % MOD

# Example usage:
n = 7
roads = [
    [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3],
    [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
    [0, 4, 5], [4, 6, 2]
]
print(countPaths(n, roads))  # Output: 4

n = 6
roads = [
    [0, 5, 8], [0, 2, 2], [0, 1, 1], [1, 3, 3],
    [1, 2, 3], [2, 5, 6], [3, 4, 2], [4, 5, 2]
]
print(countPaths(n, roads))  # Output: 3
    