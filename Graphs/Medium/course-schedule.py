from collections import deque, defaultdict

def findOrder(n, m, prerequisites):
    # Create an adjacency list for the graph
    adj_list = defaultdict(list)
    # In-degree array
    in_degree = [0] * n
    
    # Fill the adjacency list and in-degree array
    for u, v in prerequisites:
        adj_list[v].append(u)
        in_degree[u] += 1
    
    # Queue to maintain nodes with 0 in-degree
    queue = deque()
    
    # Initialize the queue with nodes having 0 in-degree
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    # List to store the topological order
    topological_order = []
    
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        
        # Reduce the in-degree of adjacent nodes
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If topological order contains all nodes, return it
    if len(topological_order) == n:
        return topological_order
    else:
        return []

# Example Test Cases
n1, m1 = 2, 1
prerequisites1 = [[1, 0]]
print(1 if findOrder(n1, m1, prerequisites1) else 0)  # Output: 1

n2, m2 = 4, 4
prerequisites2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(1 if findOrder(n2, m2, prerequisites2) else 0)  # Output: 1
