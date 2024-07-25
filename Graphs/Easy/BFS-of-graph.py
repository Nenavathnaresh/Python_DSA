from collections import deque

def bfsOfGraph(V, adj):
    # List to store the BFS traversal result
    bfs_traversal = []

    # Queue for BFS
    queue = deque([0])
    
    # List to keep track of visited nodes
    visited = [False] * V
    
    # Mark the 0th node as visited
    visited[0] = True

    while queue:
        # Dequeue a vertex from queue and add it to the result
        current_node = queue.popleft()
        bfs_traversal.append(current_node)

        # Get all adjacent vertices of the dequeued vertex current_node
        for neighbor in adj[current_node]:
            if not visited[neighbor]:
                # If a neighbor has not been visited, mark it visited and enqueue it
                visited[neighbor] = True
                queue.append(neighbor)

    return bfs_traversal

# Example 1
V1 = 5
E1 = 4
adj1 = [[1, 2, 3], [], [4], [], []]
print(bfsOfGraph(V1, adj1))  # Output: [0, 1, 2, 3, 4]

# Example 2
V2 = 3
E2 = 2
adj2 = [[1, 2], [], []]
print(bfsOfGraph(V2, adj2))  # Output: [0, 1, 2]
