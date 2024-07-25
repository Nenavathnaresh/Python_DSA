# ...............................By using DFS...............................
def isCycle(V, adj):
    # Helper function for DFS
    def dfs(node, visited, parent):
        # Mark the current node as visited
        visited[node] = True
        
        # Explore each neighbor of the current node
        for neighbor in adj[node]:
            if not visited[neighbor]:
                # If the neighbor hasn't been visited, recurse with current node as parent
                if dfs(neighbor, visited, node):
                    return True
            elif neighbor != parent:
                # If the neighbor is visited and isn't the parent, a cycle is detected
                return True
        
        return False

    # Initialize visited list for all vertices
    visited = [False] * V

    # Check for cycles in each disconnected component
    for i in range(V):
        if not visited[i]:  # If node i hasn't been visited
            if dfs(i, visited, -1):
                return 1  # Cycle detected

    return 0  # No cycle found

# Example 1
V1 = 5
E1 = 5
adj1 = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
print(isCycle(V1, adj1))  # Output: 1

# Example 2
V2 = 4
E2 = 2
adj2 = [[], [2], [1, 3], [2]]
print(isCycle(V2, adj2))  # Output: 0


# ............................................ By using BFS....................................

from collections import deque

def isCycle(V, adj):
    # Helper function for BFS
    def bfs(start, visited):
        # Queue to store (node, parent) pair
        queue = deque([(start, -1)])
        visited[start] = True

        while queue:
            current_node, parent = queue.popleft()

            # Check each neighbor of the current node
            for neighbor in adj[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, current_node))
                elif neighbor != parent:
                    # If visited and not the parent, cycle detected
                    return True

        return False

    # Initialize visited list
    visited = [False] * V

    # Check for cycles in each disconnected component
    for i in range(V):
        if not visited[i]:  # If node i hasn't been visited
            if bfs(i, visited):
                return 1  # Cycle detected

    return 0  # No cycle found

# Example 1
V1 = 5
E1 = 5
adj1 = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
print(isCycle(V1, adj1))  # Output: 1

# Example 2
V2 = 4
E2 = 2
adj2 = [[], [2], [1, 3], [2]]
print(isCycle(V2, adj2))  # Output: 0
