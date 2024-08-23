def countOfNodes(graph, n):
    # Initialize an array to track the level of each node
    level = [-1] * (n + 1)
    
    # BFS or DFS to determine the level of each node
    from collections import deque
    queue = deque([1])
    level[1] = 0
    even_count = 0
    odd_count = 0
    
    while queue:
        node = queue.popleft()
        current_level = level[node]
        
        # Count based on the level
        if current_level % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        # Traverse the neighbors
        for neighbor in graph[node]:
            if level[neighbor] == -1:
                level[neighbor] = current_level + 1
                queue.append(neighbor)
    
    # Calculate pairs with even distances
    even_pairs = even_count * (even_count - 1) // 2
    odd_pairs = odd_count * (odd_count - 1) // 2
    
    return even_pairs + odd_pairs

# Example usage:
n = 5
graph = [[], [2, 4], [1, 3], [2], [1, 5], [4]]
print(countOfNodes(graph, n))  # Output: 4

n = 3
graph = [[], [2], [1, 3], [2]]
print(countOfNodes(graph, n))  # Output: 1
