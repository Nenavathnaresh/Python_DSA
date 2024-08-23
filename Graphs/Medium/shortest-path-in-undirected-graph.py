from collections import deque, defaultdict

def shortestPath(n, m, edges, src):
    # Initialize the adjacency list
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Initialize distances array
    distances = [-1] * n
    distances[src] = 0
    
    # BFS
    queue = deque([src])
    
    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        
        # Visit all neighbors
        for neighbor in adj_list[node]:
            if distances[neighbor] == -1:  # If not visited
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    
    return distances

# Example 1:
n = 9
m = 10
edges = [[0, 1], [0, 3], [3, 4], [4, 5], [5, 6], [1, 2], [2, 6], [6, 7], [7, 8], [6, 8]]
src = 0
print(shortestPath(n, m, edges, src))  # Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]

# Example 2:
n = 4
m = 2
edges = [[1, 3], [3, 0]]
src = 3
print(shortestPath(n, m, edges, src))  # Output: [1, 1, -1, 0]
