class Solution:
    def minimumEdgeRemove(self, n, edges):
        from collections import defaultdict
        
        # Create adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Initialize a list to store the size of each subtree
        subtree_size = [0] * (n + 1)
        removable_edges = 0
        
        # DFS function to compute subtree sizes
        def dfs(node, parent):
            nonlocal removable_edges
            subtree_size[node] = 1  # count the node itself
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    subtree_size[node] += subtree_size[neighbor]
                    # If the size of the neighbor subtree is even, it can be disconnected
                    if subtree_size[neighbor] % 2 == 0:
                        removable_edges += 1
        
        # Start DFS from the root node (1), assuming 1 is the root
        dfs(1, -1)
        
        return removable_edges

# Example usage:
sol = Solution()
print(sol.minimumEdgeRemove(10, [[2, 1], [3, 1], [4, 3], [5, 2], [6, 1], [7, 2], [8, 6], [9, 8], [10, 8]]))  # Output: 2
print(sol.minimumEdgeRemove(4, [[2, 1], [4, 2], [1, 3]]))  # Output: 1
