from collections import defaultdict

# Function to check if strings can be chained to form a circle
def canFormCircle(arr):
    def dfs(v, visited):
        visited.add(v)
        for neighbor in adj[v]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    
    # Step 1: Build the graph
    adj = defaultdict(list)  # adjacency list
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    # Traverse the array to populate in_degree, out_degree, and adjacency list
    for word in arr:
        first = word[0]
        last = word[-1]
        adj[first].append(last)
        out_degree[first] += 1
        in_degree[last] += 1
    
    # Step 2: Check if in-degree equals out-degree for every vertex
    all_chars = set(in_degree.keys()).union(set(out_degree.keys()))
    for char in all_chars:
        if in_degree[char] != out_degree[char]:
            return 0  # Can't form a circle if in-degree and out-degree don't match
    
    # Step 3: Check if all vertices with edges form a strongly connected component
    # Use DFS to check connectivity from a starting vertex
    visited = set()
    start_vertex = arr[0][0]  # Start from the first character of the first string
    dfs(start_vertex, visited)
    
    # Check if all nodes that have edges are visited
    for char in all_chars:
        if char in out_degree and char not in visited:
            return 0  # If there's a character not visited, it's not strongly connected
    
    return 1  # All conditions are satisfied, so the strings can form a circle

# Test cases
arr1 = ["abc", "bcd", "cdf"]
print(canFormCircle(arr1))  # Output: 0

arr2 = ["ab", "bc", "cd", "da"]
print(canFormCircle(arr2))  # Output: 1
