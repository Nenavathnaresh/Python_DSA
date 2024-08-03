import heapq

def spanningTree(V, adj):
    # Min-heap to store the minimum weight edge at each step
    min_heap = []
    
    # Initialize the visited array to track which vertices are included in the MST
    visited = [False] * V
    
    # Starting from vertex 0 (or any arbitrary vertex)
    # Push the starting vertex with edge weight 0 to start Prim's algorithm
    heapq.heappush(min_heap, (0, 0))  # (weight, vertex)
    
    # Variable to store the total weight of the MST
    mst_weight = 0
    
    while min_heap:
        # Extract the vertex with the smallest edge weight
        weight, current_vertex = heapq.heappop(min_heap)
        
        # If the current vertex is already visited, skip it
        if visited[current_vertex]:
            continue
        
        # Mark the current vertex as visited
        visited[current_vertex] = True
        
        # Add the edge weight to the total MST weight
        mst_weight += weight
        
        # Explore all adjacent vertices
        for neighbor, edge_weight in adj[current_vertex]:
            # If the neighbor vertex is not visited, push the edge to the heap
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))
    
    return mst_weight

# Example 1
V1 = 3
edges1 = [[(1, 5), (2, 1)], [(0, 5), (2, 3)], [(0, 1), (1, 3)]]
result1 = spanningTree(V1, edges1)
print(result1)  # Expected Output: 4

# Example 2
V2 = 2
edges2 = [[(1, 5)], [(0, 5)]]
result2 = spanningTree(V2, edges2)
print(result2)  # Expected Output: 5
