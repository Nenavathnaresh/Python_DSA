# ................................. using DFS ..........................

def topoSort(V, adj):
    # Helper function for DFS traversal
    def dfs(node, visited, stack):
        # Mark the node as visited
        visited[node] = True

        # Visit all the neighbors
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)

        # Push current node to stack after visiting all its neighbors
        stack.append(node)

    # Initialize visited list and stack
    visited = [False] * V
    stack = []

    # Perform DFS from each unvisited node
    for i in range(V):
        if not visited[i]:
            dfs(i, visited, stack)

    # Stack contains the topological sort in reverse order
    return stack[::-1]

# Example 1
V1 = 4
adj1 = [[], [], [3], [1, 2]]
print(topoSort(V1, adj1))  # Possible Output: [0, 2, 3, 1]

# Example 2
V2 = 6
adj2 = [[], [0], [0, 1], [2], [3], [4]]
print(topoSort(V2, adj2))  # Possible Output: [5, 4, 3, 2, 1, 0]

# ................................... Kahn's Algorithm (BFS-Based Topological Sort) ................

from collections import deque

def topoSort(V, adj):
    # Calculate indegrees of all vertices
    indegree = [0] * V
    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor] += 1

    # Queue for vertices with zero indegree
    queue = deque()
    for i in range(V):
        if indegree[i] == 0:
            queue.append(i)

    # List to store the topological order
    topo_order = []

    # Process vertices in topological order
    while queue:
        current = queue.popleft()
        topo_order.append(current)

        # Decrease indegree of neighbors
        for neighbor in adj[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Return the topological order
    return topo_order

# Example 1
V1 = 4
adj1 = [[], [], [3], [1, 2]]
print(topoSort(V1, adj1))  # Possible Output: [0, 2, 3, 1]

# Example 2
V2 = 6
adj2 = [[], [0], [0, 1], [2], [3], [4]]
print(topoSort(V2, adj2))  # Possible Output: [5, 4, 3, 2, 1, 0]
