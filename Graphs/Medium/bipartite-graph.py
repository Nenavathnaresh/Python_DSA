###################### BFS implementation ################################
from collections import deque

def isBipartite(V, adj):
    # Initialize color array
    color = [-1] * V

    # Helper function to perform BFS
    def bfs(start):
        # Queue for BFS traversal
        queue = deque([start])
        # Color the starting node with 0
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            # Traverse all adjacent nodes
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    # Color with opposite color
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # If the neighbor has the same color, graph is not bipartite
                    return False
        return True

    # Check each component
    for i in range(V):
        if color[i] == -1:
            if not bfs(i):
                return False
    
    return True

# Example usage:
V1 = 4
adj1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(isBipartite(V1, adj1))  # Output: True (1)

V2 = 3
adj2 = [[1, 2], [0, 2], [0, 1]]
print(isBipartite(V2, adj2))  # Output: False (0)

#################################### DFS implimentations ###################################
def isBipartite(V, adj):
    # Initialize color array
    color = [-1] * V

    # Helper function to perform DFS
    def dfs(node, c):
        color[node] = c
        # Traverse all adjacent nodes
        for neighbor in adj[node]:
            if color[neighbor] == -1:
                # Color with opposite color
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == color[node]:
                # If the neighbor has the same color, graph is not bipartite
                return False
        return True

    # Check each component
    for i in range(V):
        if color[i] == -1:
            if not dfs(i, 0):
                return False
    
    return True

# Example usage:
V1 = 4
adj1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(isBipartite(V1, adj1))  # Output: True (1)

V2 = 3
adj2 = [[1, 2], [0, 2], [0, 1]]
print(isBipartite(V2, adj2))  # Output: False (0)
