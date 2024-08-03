def printGraph(V, edges):
    # Initialize an adjacency list with empty lists for each vertex
    adj_list = [[] for _ in range(V)]

    # Iterate through each edge to populate the adjacency list
    for u, v in edges:
        adj_list[u].append(v)  # Add v to the adjacency list of u
        adj_list[v].append(u)  # Add u to the adjacency list of v (since the graph is undirected)

    # Sort each adjacency list for consistent ordering
    for lst in adj_list:
        lst.sort()

    return adj_list

# Example 1
V1 = 5
edges1 = [(0, 1), (0, 4), (4, 1), (4, 3), (1, 3), (1, 2), (3, 2)]
result1 = printGraph(V1, edges1)
print(result1)
# Expected Output: [[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]]

# Example 2
V2 = 4
edges2 = [(0, 3), (0, 2), (2, 1)]
result2 = printGraph(V2, edges2)
print(result2)
# Expected Output: [[2, 3], [2], [0, 1], [0]]


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def printGraph(self, V : int, edges ):
        # code here
        vertices = [[] for _ in range(V)]
        for i in range(len(edges)):
            vertices[edges[i][0]].append(edges[i][1])
            vertices[edges[i][1]].append(edges[i][0])
        return vertices