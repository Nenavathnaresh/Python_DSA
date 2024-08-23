import heapq

def minimumCost(n, k, flights):
    # Convert k to zero-based index
    k -= 1
    
    # Build the graph as an adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in flights:
        graph[u-1].append((v-1, w))
    
    # Dijkstra's algorithm
    def dijkstra(source):
        dist = [float('inf')] * n
        dist[source] = 0
        min_heap = [(0, source)]  # (cost, node)
        
        while min_heap:
            curr_cost, u = heapq.heappop(min_heap)
            
            # Process each neighbor
            for v, weight in graph[u]:
                if dist[v] > curr_cost + weight:
                    dist[v] = curr_cost + weight
                    heapq.heappush(min_heap, (dist[v], v))
        
        return dist
    
    # Get the minimum distances from the source city k
    distances = dijkstra(k)
    
    # Find the maximum distance to determine the minimum money Alex needs
    max_cost = max(distances)
    
    # If there's an unreachable city, return -1
    return -1 if max_cost == float('inf') else max_cost

# Example 1:
n = 4
k = 2
flights = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
print(minimumCost(n, k, flights))  # Output: 2

# Example 2:
n = 4
k = 3
flights = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
print(minimumCost(n, k, flights))  # Output: -1
