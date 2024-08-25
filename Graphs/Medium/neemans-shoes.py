import heapq

def exercise(N, M, A, src, dest, X):
    # Create adjacency list for the graph
    adj = [[] for _ in range(N)]
    
    for i in range(M):
        u, v, w = A[i]
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Dijkstra's algorithm to find the shortest path from src to dest
    def dijkstra(src, dest):
        dist = [float('inf')] * N
        dist[src] = 0
        min_heap = [(0, src)]  # (distance, node)
        
        while min_heap:
            current_dist, u = heapq.heappop(min_heap)
            
            if current_dist > dist[u]:
                continue
            
            for v, weight in adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[v], v))
        
        return dist[dest]
    
    # Find the shortest path from src to dest
    shortest_path = dijkstra(src, dest)
    
    # Compare the shortest path distance with X
    if shortest_path > X:
        return "Neeman's Wool Joggers"
    else:
        return "Neeman's Cotton Classics"

# Example usage:
N = 3
M = 2
src = 0
dest = 2
X = 5
A = [[0, 1, 3], [1, 2, 3]]
print(exercise(N, M, A, src, dest, X))  # Output: "Neeman's Wool Joggers"

N = 3
M = 2
src = 0
dest = 2
X = 6
A = [[0, 1, 3], [1, 2, 3]]
print(exercise(N, M, A, src, dest, X))  # Output: "Neeman's Cotton Classics"
