import heapq

def dijkstra(V, adj, S):
    # Initialize distances with infinity and set the distance for the source as 0
    dist = [float('inf')] * V
    dist[S] = 0
    
    # Min-heap priority queue to hold vertices and their distances
    priority_queue = [(0, S)]  # (distance, vertex)
    
    # While the priority queue is not empty
    while priority_queue:
        # Extract the vertex with the smallest distance
        current_distance, u = heapq.heappop(priority_queue)
        
        # If current_distance is greater than the recorded shortest path, skip it
        if current_distance > dist[u]:
            continue
        
        # Iterate over all the neighbors of the current vertex
        for neighbor in adj[u]:
            v, weight = neighbor  # v is the adjacent vertex, weight is the edge weight
            
            # Calculate the distance through the current vertex u
            new_distance = dist[u] + weight
            
            # If the new calculated distance is less than the current known distance
            if new_distance < dist[v]:
                dist[v] = new_distance
                heapq.heappush(priority_queue, (new_distance, v))
    
    return dist

# Example 1
V1 = 2
adj1 = [
    [[1, 9]],  # Node 0 is connected to node 1 with weight 9
    [[0, 9]]   # Node 1 is connected to node 0 with weight 9 (undirected)
]
S1 = 0
print(dijkstra(V1, adj1, S1))  # Output: [0, 9]

# Example 2
V2 = 3
adj2 = [
    [[1, 1], [2, 6]],  # Node 0 is connected to node 1 (weight 1) and node 2 (weight 6)
    [[2, 3], [0, 1]],  # Node 1 is connected to node 2 (weight 3) and node 0 (weight 1)
    [[1, 3], [0, 6]]   # Node 2 is connected to node 1 (weight 3) and node 0 (weight 6)
]
S2 = 2
print(dijkstra(V2, adj2, S2))  # Output: [4, 3, 0]

######################################################### Second method ####################################

import heapq  # Python's built-in priority queue

def dijkstra(graph, source):
    # Number of vertices in the graph
    n = len(graph)

    # Initialize distances with infinity
    dist = [float('inf')] * n
    dist[source] = 0  # Distance from source to itself is 0

    # Priority queue to hold vertices and their current distances
    priority_queue = [(0, source)]  # (distance, vertex)
    
    # Visited array to keep track of visited vertices
    visited = [False] * n

    while priority_queue:
        # Extract the vertex with the smallest distance
        current_distance, u = heapq.heappop(priority_queue)

        if visited[u]:
            continue

        # Mark the vertex as visited
        visited[u] = True

        # Relaxation step
        for v, weight in graph[u]:
            if not visited[v] and current_distance + weight < dist[v]:
                dist[v] = current_distance + weight
                heapq.heappush(priority_queue, (dist[v], v))

    return dist

# Example usage
graph = [
    [(1, 4), (2, 1)],  # Node 0 is connected to node 1 (weight 4) and node 2 (weight 1)
    [(3, 1)],          # Node 1 is connected to node 3 (weight 1)
    [(1, 2), (3, 5)],  # Node 2 is connected to node 1 (weight 2) and node 3 (weight 5)
    []                 # Node 3 has no outgoing edges
]

source = 0
distances = dijkstra(graph, source)
print("Shortest distances from node", source, ":", distances)

