from collections import deque

def isPossible(N, P, prerequisites):
    # Create an adjacency list using a list of lists
    adj = [[] for _ in range(N)]
    indegree = [0] * N
    
    # Build the graph
    for u, v in prerequisites:
        adj[v].append(u)
        indegree[u] += 1
    
    # Queue for BFS
    queue = deque()
    
    # Initialize the queue with nodes that have 0 indegree
    for i in range(N):
        if indegree[i] == 0:
            queue.append(i)
    
    count = 0
    
    # Process the queue
    while queue:
        node = queue.popleft()
        count += 1
        
        # Decrease the indegree of neighboring nodes
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # If the count of processed nodes is equal to N, then it's possible to finish all tasks
    return count == N

# Example Test Cases
N1, P1, prerequisites1 = 4, 3, [[1, 0], [2, 1], [3, 2]]
print(isPossible(N1, P1, prerequisites1))  # Output: True (Yes)

N2, P2, prerequisites2 = 2, 2, [[1, 0], [0, 1]]
print(isPossible(N2, P2, prerequisites2))  # Output: False (No)
