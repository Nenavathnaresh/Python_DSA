import heapq

def findCity(n, m, edges, distanceThreshold):
    def dijkstra(start):
        distances = [float('inf')] * n
        distances[start] = 0
        pq = [(0, start)]  # (distance, node)
        
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            
            if current_dist > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances
    
    # Build the graph
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Find the city with the smallest number of reachable cities
    minReachable = n
    resultCity = -1
    
    for i in range(n):
        distances = dijkstra(i)
        reachable = sum(1 for d in distances if d <= distanceThreshold)
        if reachable < minReachable or (reachable == minReachable and i > resultCity):
            minReachable = reachable
            resultCity = i
    
    return resultCity

# Example Usage
n = 4
m = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
print(findCity(n, m, edges, distanceThreshold))  # Output: 3

n = 5
m = 6
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distanceThreshold = 2
print(findCity(n, m, edges, distanceThreshold))  # Output: 0


################################################################################################

def findCity(n, m, edges, distanceThreshold):
    # Initialize distance matrix
    inf = float('inf')
    distance = [[inf] * n for _ in range(n)]
    
    # Set the distance to self as 0
    for i in range(n):
        distance[i][i] = 0
    
    # Fill in the initial distances based on the edges
    for u, v, w in edges:
        distance[u][v] = w
        distance[v][u] = w
    
    # Floyd-Warshall Algorithm to find all pairs shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    # Find the city with the minimum number of reachable cities within the distanceThreshold
    min_count = inf
    result_city = -1
    
    for i in range(n):
        count = 0
        for j in range(n):
            if distance[i][j] <= distanceThreshold:
                count += 1
        
        # Check for the minimum count and if there's a tie, select the city with the greater label
        if count <= min_count:
            min_count = count
            result_city = i
    
    return result_city

# Example Usage:
n = 4
m = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
print(findCity(n, m, edges, distanceThreshold))  # Output: 3
