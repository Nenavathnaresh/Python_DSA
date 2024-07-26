# ......................... By DFS .......................................

def isCyclic(V, adj):
    # Helper function for DFS to detect cycles
    def dfs(node, visited, recStack):
        # Mark the current node as visited and add to the recursion stack
        visited[node] = True
        recStack[node] = True

        # Recur for all neighbors
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, recStack):
                    return True
            elif recStack[neighbor]:
                return True

        # Remove the node from recursion stack
        recStack[node] = False
        return False

    # Initialize visited and recursion stack
    visited = [False] * V
    recStack = [False] * V

    # Check for cycles in different DFS trees
    for i in range(V):
        if not visited[i]:
            if dfs(i, visited, recStack):
                return 1  # Cycle found

    return 0  # No cycle found

# Example 1
V1 = 4
adj1 = [[1], [2], [3], [0]]
print(isCyclic(V1, adj1))  # Output: 1

# Example 2
V2 = 4
adj2 = [[1], [2], [3], []]
print(isCyclic(V2, adj2))  # Output: 0


# ..................................... By BFS .........................................

from collections import deque

def isCyclic(V, adj):
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

    # Process vertices in topological order
    count = 0
    while queue:
        current = queue.popleft()
        count += 1

        # Decrease indegree of neighbors
        for neighbor in adj[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If count is less than V, there's a cycle
    if count == V:
        return 0  # No cycle
    else:
        return 1  # Cycle found

# Example 1
V1 = 4
adj1 = [[1], [2], [3], [0]]
print(isCyclic(V1, adj1))  # Output: 1

# Example 2
V2 = 4
adj2 = [[1], [2], [3], []]
print(isCyclic(V2, adj2))  # Output: 0
