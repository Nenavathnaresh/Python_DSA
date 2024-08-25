from collections import deque, defaultdict

def minTime(N, M, duration, dependencies):
    # Create adjacency list and in-degree array
    adj = defaultdict(list)
    in_degree = [0] * N
    
    for u, v in dependencies:
        adj[u].append(v)
        in_degree[v] += 1
    
    # Initialize the DP array with duration times
    dp = duration[:]
    
    # Queue for topological sort
    queue = deque()
    
    # Start with nodes that have zero in-degree
    for i in range(N):
        if in_degree[i] == 0:
            queue.append(i)
    
    visited_count = 0
    
    while queue:
        u = queue.popleft()
        visited_count += 1
        
        for v in adj[u]:
            # Update the dp value for node v
            dp[v] = max(dp[v], dp[u] + duration[v])
            in_degree[v] -= 1
            
            if in_degree[v] == 0:
                queue.append(v)
    
    # If we visited all nodes, return the max time, otherwise return -1 (cycle detected)
    return max(dp) if visited_count == N else -1

# Example usage:
N = 6
M = 6
duration = [1, 2, 3, 1, 3, 2]
dependencies = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
print(minTime(N, M, duration, dependencies))  # Output: 8

N = 3
M = 3
duration = [5, 5, 5]
dependencies = [[0, 1], [1, 2], [2, 0]]
print(minTime(N, M, duration, dependencies))  # Output: -1
