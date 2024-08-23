def eulerPath(N, graph):
    # Count vertices with odd degree
    odd_count = 0
    
    for i in range(N):
        degree = sum(graph[i])  # Degree of vertex i
        
        if degree % 2 != 0:
            odd_count += 1
    
    # Eulerian Path exists if there are exactly 0 or 2 vertices with odd degree
    if odd_count == 0 or odd_count == 2:
        return 1
    else:
        return 0

# Example 1:
N = 5
graph = [[0, 1, 0, 0, 1], 
         [1, 0, 1, 1, 0], 
         [0, 1, 0, 1, 0], 
         [0, 1, 1, 0, 0], 
         [1, 0, 0, 0, 0]]
print(eulerPath(N, graph))  # Output: 1

# Example 2:
N = 5
graph = [[0, 1, 0, 1, 1], 
         [1, 0, 1, 0, 1], 
         [0, 1, 0, 1, 1], 
         [1, 0, 1, 0, 0], 
         [1, 1, 1, 0, 0]]
print(eulerPath(N, graph))  # Output: 0
