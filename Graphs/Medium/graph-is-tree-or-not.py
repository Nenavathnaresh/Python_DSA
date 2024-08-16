def isTree(N, M, G):
    if M != N - 1:
        return 0  # Not a tree, because it doesn't have N-1 edges
    
    from collections import defaultdict, deque
    
    # Create adjacency list
    adj = defaultdict(list)
    for u, v in G:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * N
    def bfs(start):
        queue = deque([(start, -1)])  # (current_node, parent)
        visited[start] = True
        
        while queue:
            node, parent = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return False  # Cycle detected
        return True
    
    # Start BFS from node 0
    if not bfs(0):
        return 0
    
    # Check if all nodes are visited
    if any(not visited[i] for i in range(N)):
        return 0
    
    return 1

# Example usage:
N = 4
M = 3
G = [[0, 1], [1, 2], [1, 3]]
print(isTree(N, M, G))  # Output: 1

N = 4
M = 3
G = [[0, 1], [1, 2], [2, 0]]
print(isTree(N, M, G))  # Output: 0
