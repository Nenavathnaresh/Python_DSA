from collections import deque

def findLevelOfNode(v, adj, x):
    if x >= v or x < 0:
        return -1  # Node x is out of bounds
    
    # BFS initialization
    queue = deque([0])
    levels = [-1] * v  # Initialize all levels to -1
    levels[0] = 0  # Starting node level is 0
    
    while queue:
        node = queue.popleft()
        
        for neighbor in adj[node]:
            if levels[neighbor] == -1:  # Not visited yet
                levels[neighbor] = levels[node] + 1
                queue.append(neighbor)
                
                if neighbor == x:
                    return levels[neighbor]
    
    return -1  # If x was never reached

# Example usage:
v = 5
adj = [[1, 2], [0, 3, 4], [0], [1], [1]]
x = 4
print(findLevelOfNode(v, adj, x))  # Output: 2

x = 1
print(findLevelOfNode(v, adj, x))  # Output: 1
