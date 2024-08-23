from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minTimeToBurnTree(root, target):
    if not root:
        return 0
    
    # Step 1: Map each node to its parent
    parent_map = {}
    
    def dfs(node, parent=None):
        if not node:
            return
        if parent:
            parent_map[node] = parent
        dfs(node.left, node)
        dfs(node.right, node)
    
    # Run DFS to build the parent_map
    dfs(root)
    
    # Step 2: Perform BFS from the target node
    def bfs_from_target(target_node):
        queue = deque([(target_node, 0)])  # (current node, current time)
        visited = set([target_node])
        max_time = 0
        
        while queue:
            current_node, time = queue.popleft()
            max_time = max(max_time, time)
            
            # Spread to left child
            if current_node.left and current_node.left not in visited:
                visited.add(current_node.left)
                queue.append((current_node.left, time + 1))
            
            # Spread to right child
            if current_node.right and current_node.right not in visited:
                visited.add(current_node.right)
                queue.append((current_node.right, time + 1))
            
            # Spread to parent
            if current_node in parent_map and parent_map[current_node] not in visited:
                visited.add(parent_map[current_node])
                queue.append((parent_map[current_node], time + 1))
        
        return max_time
    
    # Step 3: Find the target node and start BFS from there
    def find_target(node, target):
        if not node:
            return None
        if node.val == target:
            return node
        left_search = find_target(node.left, target)
        if left_search:
            return left_search
        return find_target(node.right, target)
    
    target_node = find_target(root, target)
    if not target_node:
        return 0
    
    return bfs_from_target(target_node)

# Example usage:
# Constructing the tree
#          1
#        /   \
#      2      3
#    /  \      \
#   4    5      6
#       / \      \
#      7   8      9
#                   \
#                   10
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right.right.right = TreeNode(9)
root.right.right.right.right = TreeNode(10)

target = 8
print(minTimeToBurnTree(root, target))  # Output: 7
